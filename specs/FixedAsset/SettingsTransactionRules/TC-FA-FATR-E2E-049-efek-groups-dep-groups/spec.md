---
id: TC-FA-FATR-E2E-049-efek-groups-dep-groups
title: "Override mengikuti perubahan Group"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r273, §4.1#r274, §9.4.2#r34, §9.2#b122, §9.2#b124, §9.2#b147, §9.2#b125]
smoke: []
dependsOn:
  - "Settings Groups: hapus dan nonaktifkan Group"
trace:
  §4.1#r273: [7, 16]
  §4.1#r274: [8, 9, 17, 18]
  §9.4.2#r34: [6, 8, 15, 17]
  §9.2#b122: [6, 15]
  §9.2#b124: [7, 16]
  §9.2#b147: [6, 15]
  §9.2#b125: [8, 9, 17, 18]
anchor: [3, 12]
coverage:
  web: automated
---

# Override mengikuti perubahan Group

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan akses penuh ke Group.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-049-1: Category Name `Cooling Equipment {runId}`; Category leaf tempat override dibuat.
  - DU-049-2: Group Name `Depot Surabaya {runId}`; Group yang akan dihapus.
  - DU-049-3: Group Name `Depot Medan {runId}`; Group yang akan dinonaktifkan.
  - DU-049-4: Override Target `Depot Surabaya {runId}`, Scope `Group`, Category `Cooling Equipment {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Group untuk Group yang akan dihapus.
  - DU-049-5: Override Target `Depot Medan {runId}`, Scope `Group`, Category `Cooling Equipment {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Group untuk Group yang akan dinonaktifkan.

## Test Steps

### Override tetap tampil dan tidak berlaku sesudah Group dihapus
1. Masuk sebagai Default User
2. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi override untuk target `Depot Surabaya {runId}` tampil di tabel Overrides
4. Hapus Group `Depot Surabaya {runId}`
5. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
6. Verifikasi override untuk target `Depot Surabaya {runId}` tetap tersimpan dan tampil di tabel Overrides
7. Verifikasi nama terakhir target `Depot Surabaya {runId}` tetap tampil pada baris override itu
8. Verifikasi `Not applied` tampil pada sel Target baris override untuk `Depot Surabaya {runId}`
9. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target

### Override tetap tampil dan tidak berlaku sesudah Group dinonaktifkan
10. Masuk sebagai Default User
11. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
12. Verifikasi override untuk target `Depot Medan {runId}` tampil di tabel Overrides
13. Nonaktifkan Group `Depot Medan {runId}`
14. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
15. Verifikasi override untuk target `Depot Medan {runId}` tetap tersimpan dan tampil di tabel Overrides
16. Verifikasi nama terakhir target `Depot Medan {runId}` tetap tampil pada baris override itu
17. Verifikasi `Not applied` tampil pada sel Target baris override untuk `Depot Medan {runId}`
18. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target
