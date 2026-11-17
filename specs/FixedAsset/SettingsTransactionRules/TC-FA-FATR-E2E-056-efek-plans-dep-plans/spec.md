---
id: TC-FA-FATR-E2E-056-efek-plans-dep-plans
title: "Perubahan plan tercermin di Transaction Settings"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.4.2#r54", "§9.4.4#r55", "§9.4.4#r57", "§9.4.4#r58", "§9.10.1#b9", "§9.10.2#b7", "§9.10.3#b2", "§11#r2", "§9.2#b556", "§9.2#b558", "§9.2#b559", "§9.8#r15"]
smoke: ["§9.2#b556", "§9.2#b558", "§9.2#b559", "§9.8#r15"]
dependsOn:
  - "Admin Console: Plans & Features"
trace:
  "§9.4.2#r54": [16, 24]
  "§9.4.4#r55": 16
  "§9.4.4#r57": 33
  "§9.4.4#r58": 50
  "§9.10.1#b9": [16, 24]
  "§9.10.2#b7": [31, 33, 41]
  "§9.10.3#b2": [48, 50, 58]
  "§11#r2": [13, 14, 31, 48]
  "§9.2#b556": 16
  "§9.2#b558": 33
  "§9.2#b559": 50
  "§9.8#r15": 16
anchor: [3]
coverage:
  web: automated
---

# Perubahan plan tercermin di Transaction Settings

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan Principal yang dapat mengubah plan di Admin Console.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-056-1: Entitas Name `Entitas Plan {runId}`, Approval Workflow `ON`, Feature Suite Borrowing `Full`, Feature Suite Assignment `Full`; entitas khusus spec ini dengan Approval Workflow ON, level Feature Suite Borrowing Full, dan level Feature Suite Assignment Full.
  - DU-056-2: Category Name `Plan Equipment {runId}`, Require approval Assign `ON`, Self service Borrow `ON` dan Duration unit `Hours`; Category leaf dengan nilai tersimpan field bergerbang.
  - DU-056-3: Group Name `Plan Team {runId}`; Group target override.
  - DU-056-4: Override Target `Plan Team {runId}`, Scope `Group`, Category `Plan Equipment {runId}`, Transaction `Assign`, Require approval `ON`; override Group dengan field bergerbang Require approval.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Plan {runId}` yang tidak dipakai spec lain, karena yang diubah adalah plan entitas.
  - Plan `Entitas Plan {runId}` adalah plan khusus spec ini yang hanya dipakai entitas khusus itu, bukan plan bersama dengan entitas lain.
  - Plan entitas khusus ini memiliki Approval Workflow `ON`, level Feature Suite Borrowing `Full`, dan level Feature Suite Assignment `Full`.
  - Category `Plan Equipment {runId}` menyimpan Require approval Assign `ON`, Self service Borrow `ON` dan Duration unit `Hours`.

## Test Steps
### Toggle Approval Workflow dicabut tidak masuk Changelog dan nilai tersimpan berlaku saat ON kembali
1. Masuk sebagai Default User
2. Buka tab `Assign` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi field Require approval bernilai `ON` dan dapat diubah
4. Buka dialog Changelog dari header halaman Transaction Settings
5. Catat jumlah entri Changelog
6. Tutup dialog Changelog
7. Masuk sebagai Principal
8. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
9. Ubah toggle Approval Workflow menjadi `OFF`
10. Simpan perubahan plan
11. Masuk sebagai Default User
12. Buka tab `Assign` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
13. Verifikasi field Require approval disabled dengan nilai tersimpan `ON` dipertahankan
14. Verifikasi baris override untuk `Plan Team {runId}` tampil dengan Badge `Not applied` dan tooltip `Requires Approval Workflow on your plan.`
15. Buka dialog Changelog dari header halaman Transaction Settings
16. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat sebelum perubahan plan
17. Tutup dialog Changelog
18. Masuk sebagai Principal
19. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
20. Ubah toggle Approval Workflow menjadi `ON`
21. Simpan perubahan plan
22. Masuk sebagai Default User
23. Buka tab `Assign` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
24. Verifikasi field Require approval dapat diubah dan bernilai `ON` tersimpan langsung berlaku

### Level Feature Suite Borrowing diturunkan tidak masuk Changelog dan nilai tersimpan berlaku saat Full kembali
25. Masuk sebagai Principal
26. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
27. Pilih level Feature Suite Borrowing `Basic`
28. Simpan perubahan plan
29. Masuk sebagai Default User
30. Buka tab `Borrow` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
31. Verifikasi field Self service dan Duration unit disabled dengan nilai tersimpan `ON` dan `Hours` dipertahankan
32. Buka dialog Changelog dari header halaman Transaction Settings
33. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat sebelum perubahan plan
34. Tutup dialog Changelog
35. Masuk sebagai Principal
36. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
37. Pilih level Feature Suite Borrowing `Full`
38. Simpan perubahan plan
39. Masuk sebagai Default User
40. Buka tab `Borrow` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
41. Verifikasi field Self service dan Duration unit dapat diubah dengan nilai tersimpan `ON` dan `Hours` langsung berlaku

### Level Feature Suite Assignment diturunkan tidak masuk Changelog dan nilai tersimpan berlaku saat Full kembali
42. Masuk sebagai Principal
43. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
44. Pilih level Feature Suite Assignment `None`
45. Simpan perubahan plan
46. Masuk sebagai Default User
47. Buka node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
48. Verifikasi tab `Assign` tampil disabled dan tidak dapat dibuka
49. Buka dialog Changelog dari header halaman Transaction Settings
50. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat sebelum perubahan plan
51. Tutup dialog Changelog
52. Masuk sebagai Principal
53. Buka Plans & Features di Admin Console untuk plan `Entitas Plan {runId}`
54. Pilih level Feature Suite Assignment `Full`
55. Simpan perubahan plan
56. Masuk sebagai Default User
57. Buka tab `Assign` pada node Category `Plan Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
58. Verifikasi tab `Assign` dapat dibuka dan field Require approval dapat diubah dengan nilai tersimpan `ON` langsung berlaku
