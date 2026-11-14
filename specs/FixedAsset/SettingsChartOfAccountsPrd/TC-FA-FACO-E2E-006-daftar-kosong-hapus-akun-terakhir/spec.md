---
id: TC-FA-FACO-E2E-006-daftar-kosong-hapus-akun-terakhir
title: "Menghapus akun terakhir menampilkan empty state Account List"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["ST-16", "EB-EDG-2"]
smoke: []
dependsOn: []
trace:
  "ST-16": [4, 5]
  "EB-EDG-2": 4
anchor: 1
coverage:
  web: automated
---

# Menghapus akun terakhir menampilkan empty state Account List

## Prerequisites
- Aktor: pengguna Total Control di entitas khusus spec ini.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-006-1: entitas khusus `Entitas Uji Kosong {runId}`, hanya dipakai spec ini.
  - DU-006-2: satu-satunya akun di entitas ini, Account Code `E1-{runId}`, Account Name `Akun Terakhir {runId}`, Account Function `Asset Cost`, Status `Active`. Entitas ini tidak memiliki akun lain.

## Test Steps
### Menghapus akun terakhir menampilkan empty state
1. Verifikasi baris `E1-{runId}` tampil di tabel
2. Klik `⋯` pada baris `E1-{runId}` > `Delete`
3. Klik `[Delete]` pada dialog `Delete Account`
4. Verifikasi empty state dengan judul `No account yet` tampil di tabel
5. Verifikasi empty state dengan deskripsi `Get started by creating your first account.` tampil di tabel
