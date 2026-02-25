# 📖 Incident Response & Recovery Runbook

This guide provides step-by-step instructions for identifying and resolving common issues within the ShopMicro Production Platform.

---

## 🚨 Incident 1: Pod in `CrashLoopBackOff` (Memory/OOM)
**Symptom**: Grafana shows a pod's memory usage hitting the "Limit" line, and `kubectl get pods` shows a status of `CrashLoopBackOff`.

### Recovery Steps:
1.  **Confirm OOM**: Run `kubectl describe pod <pod-name> -n shopmicro` and look for `Reason: OomKilled`.
2.  **Immediate Fix**: 
    * Open the corresponding YAML in `k8s/` (e.g., `frontend.yaml`).
    * Increase the `memory` limit (e.g., from `256Mi` to `512Mi`).
3.  **Apply**: `kubectl apply -f k8s/<file>.yaml -n shopmicro`.
4.  **Verify**: Ensure the pod reaches `1/1 READY` status.

---

## 🚨 Incident 2: Pods are `Running` but `0/1 READY`
**Symptom**: The pod is active, but the Readiness Probe is failing with a `404` or `Connection Refused`.

### Recovery Steps:
1.  **Check Probes**: Run `kubectl describe pod <pod-name> -n shopmicro` and check the "Events" section for probe failures.
2.  **Diagnostic**: Check if the application path exists or if the app needs more time to start.
3.  **Fix**:
    * Update the `readinessProbe` path in the manifest if it's incorrect (e.g., from `/` to `/health`).
    * Increase `initialDelaySeconds` if the app is slow to boot.
4.  **Apply**: `kubectl apply -f k8s/<file>.yaml -n shopmicro`.

---

## 🚨 Incident 3: Total Namespace Failure
**Symptom**: All services in the `shopmicro` namespace are unreachable.

### Recovery Steps:
1.  **Check Infrastructure**: Verify that Postgres and Redis are running, as the backend depends on them.
2.  **Full Restart**: If the state is corrupted, perform a sequenced restart:
    ```bash
    kubectl delete -f k8s/backend.yaml -f k8s/frontend.yaml -n shopmicro
    kubectl apply -f k8s/backend.yaml -f k8s/frontend.yaml -n shopmicro
    ```
3.  **Database Check**: Ensure the `shopmicro-secrets` are still present: `kubectl get secrets -n shopmicro`.

---

## 🛠️ General Maintenance
* **Viewing Logs**: `kubectl logs -f <pod-name> -n shopmicro`
* **Checking Resource Quota**: View the **Compute Resources / Cluster** dashboard in Grafana to ensure the namespace isn't exceeding its allocated limits.