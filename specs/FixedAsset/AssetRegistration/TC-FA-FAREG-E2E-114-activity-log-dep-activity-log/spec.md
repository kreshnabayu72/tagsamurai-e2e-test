---
id: TC-FA-FAREG-E2E-114-activity-log-dep-activity-log
title: "Activity Log: entri registrasi terbaca"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-XM-2@activity-log, FAREG-LOGIC-21b]
smoke: [FAREG-LOGIC-21b]
dependsOn: ["Activity Log: daftar entri"]
trace:
  EB-XM-2@activity-log: 7
  FAREG-LOGIC-21b: 7
anchor: []
coverage:
  web: automated
---

# Activity Log: entri registrasi terbaca

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Log {runId}`.
- Layar awal: Activity Log.
- Data:
  - DU-114-1: Group `Gudang Log {runId}`, ada di entitas aktor.
  - DU-114-2: batch Draft `Gudang Log {runId}` berisi 1 Item Asset Name `Rak Log {runId}` dengan TAG Type `Non-TAG`, Brand `Olympic`, Model `No Model`, Quantity `1`.

## Test Steps

### Download daftar Draft tercatat di Activity Log
1. Catat entri teratas di Activity Log
2. Buka Fixed Asset > Assets > Registration > Draft
3. Klik `[Download]`
4. Pilih `Download as CSV`
5. Buka Activity Log
6. Muat ulang halaman
7. Verifikasi entri baru berbentuk `[User] exported [Filename]` dengan User pengguna yang mengunduh dan Filename sama dengan nama berkas yang diunduh pada langkah 4 tampil di atas entri yang dicatat
