---
id: TC-FA-FAREG-E2E-094-entitas-suspended-expired
title: "Entitas Suspended atau Expired: aksi tulis diblok"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-21d", "EB-AKS-7", "F-FAREG-05.k3"]
smoke: ["F-FAREG-05.k3"]
dependsOn: []
trace:
  "FAREG-LOGIC-21d": [6, 13]
  "EB-AKS-7": [6, 7, 13, 14]
  "F-FAREG-05.k3": [6, 13]
coverage:
  web: automated
---

# Entitas Suspended atau Expired: aksi tulis diblok

## Prerequisites
- Aktor: Hana S (Total Control entitas `Klien Suspended {runId}`), lalu Eko E (Total Control entitas `Klien Expired {runId}`).
- Layar awal: Fixed Asset > Assets.
- Data:
  - Spec ini memakai entitas khusus `Klien Suspended {runId}` dan `Klien Expired {runId}` yang tidak dipakai spec lain.
  - DU-094-1: Client `Klien Suspended {runId}` berstatus Suspended.
  - DU-094-2: Client `Klien Expired {runId}` berstatus Expired.
  - DU-094-3: Batch Draft di entitas `Klien Suspended {runId}` dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-094-4: Batch Draft di entitas `Klien Expired {runId}` dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-094-5: Hana S (Total Control, seluruh entitas `Klien Suspended {runId}`).
  - DU-094-6: Eko E (Total Control, seluruh entitas `Klien Expired {runId}`).
  - Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`) adalah pembuat batch DU-094-3 dan DU-094-4 di entitasnya masing-masing.

## Test Steps

### Entitas Suspended menolak Delete draft dengan copy khusus
1. Masuk sebagai Hana S pada entitas `Klien Suspended {runId}`
2. Klik tab `Registration`
3. Ketik Search `Gudang 1 {runId}`, tekan Enter
4. Klik row action `Delete` pada baris `Gudang 1 {runId}`
5. Klik `[Delete]` pada dialog `Delete Draft`
6. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada entitas Suspended
7. Verifikasi baris Group `Gudang 1 {runId}` tetap tampil di sub tab `Draft` pada entitas Suspended

### Entitas Expired menolak Delete draft dengan copy yang sama
8. Masuk sebagai Eko E pada entitas `Klien Expired {runId}`
9. Klik tab `Registration`
10. Ketik Search `Gudang 1 {runId}`, tekan Enter
11. Klik row action `Delete` pada baris `Gudang 1 {runId}`
12. Klik `[Delete]` pada dialog `Delete Draft`
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada entitas Expired
14. Verifikasi baris Group `Gudang 1 {runId}` tetap tampil di sub tab `Draft` pada entitas Expired
