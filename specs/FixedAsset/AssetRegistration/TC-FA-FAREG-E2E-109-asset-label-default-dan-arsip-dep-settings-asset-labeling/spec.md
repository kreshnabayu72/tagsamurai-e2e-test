---
id: TC-FA-FAREG-E2E-109-asset-label-default-dan-arsip-dep-settings-asset-labeling
title: "Asset Label default dan Asset Label yang diarsipkan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-08f, FAREG-LOGIC-16d]
smoke: []
dependsOn: ["Settings Asset Labeling: master Asset Label"]
trace:
  FAREG-LOGIC-16d: [10, 13, 15, 47, 52, 68]
  FAREG-LOGIC-08f: [22, 24, 30, 32]
anchor: []
coverage:
  web: automated
---

# Asset Label default dan Asset Label yang diarsipkan

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Label {runId}`, `Gudang Label Arsip {runId}`, `Gudang Label Hapus {runId}`, `Gudang Label Aktif {runId}`, dan `Gudang Label Approval {runId}`, serta capability Update pada node Group `Gudang Label Approval {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu pengarsipan dan penghapusan Asset Label.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-109-1: Group `Gudang Label {runId}`, ada di entitas aktor.
  - DU-109-2: Group `Gudang Label Arsip {runId}`, ada di entitas aktor.
  - DU-109-3: Asset Name `Router Label {runId}` dengan TAG Type `Non-TAG`, Brand `Cisco`, Model `ISR 4331`, dan Asset Label default `Label Default {runId}`.
  - DU-109-4: Asset Label `Label Umum {runId}`, bukan default, ada di master Asset Label.
  - DU-109-5: Asset Label `Label Arsip {runId}`, ada di master Asset Label.
  - DU-109-6: batch Draft `Gudang Label Arsip {runId}` berisi 1 Item Asset Name `Switch Label {runId}` dengan TAG Type `Non-TAG`, Brand `Cisco`, Model `Catalyst 9200`, Quantity `1`, dan Asset labels `Label Arsip {runId}` terpilih.
  - DU-109-7: Group `Gudang Label Hapus {runId}`, ada di entitas aktor.
  - DU-109-8: Group `Gudang Label Aktif {runId}`, ada di entitas aktor.
  - DU-109-9: Group `Gudang Label Approval {runId}`, ada di entitas aktor.
  - DU-109-10: Asset Label `Label Hapus {runId}`, ada di master Asset Label.
  - DU-109-11: batch Draft `Gudang Label Hapus {runId}` berisi 1 Item Asset Name `Switch Label {runId}` dengan TAG Type `Non-TAG`, Brand `Cisco`, Model `Catalyst 9200`, Quantity `1`, dan Asset labels `Label Hapus {runId}` terpilih.
- Kondisi:
  - approval registrasi pada Group `Gudang Label Aktif {runId}` bernilai OFF.
  - approval registrasi pada Group `Gudang Label Approval {runId}` bernilai ON.
  - sisa kuota Group dan tenant mencukupi untuk 1 aset pada masing-masing Group.

## Test Steps

### Asset Label default ditempel otomatis dan tidak dapat dilepas
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Label {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Router Label {runId}`
5. Pilih Brand `Cisco`
6. Pilih Model `ISR 4331`
7. Isi Quantity `1`
8. Klik tab `Asset`
9. Klik row action `Detail` pada baris aset pertama
10. Verifikasi Asset labels memuat `Label Default {runId}`
11. Lepas Asset label `Label Default {runId}`[^drift-1]
12. Pilih Asset labels `Label Umum {runId}`
13. Verifikasi Asset labels memuat `Label Umum {runId}` dan `Label Default {runId}`
14. Lepas Asset label `Label Umum {runId}`
15. Verifikasi Asset labels hanya memuat `Label Default {runId}`

### Asset Label yang diarsipkan dilepas dari draft dengan peringatan
16. Klik `[Cancel]`
17. Klik `[Leave]` pada dialog Unsaved Changes
18. Admin mengarsipkan Asset Label `Label Arsip {runId}`
19. Ketik Search `Gudang Label Arsip {runId}`, tekan Enter
20. Klik row action `Edit` pada baris batch `Gudang Label Arsip {runId}`
21. Klik tab `Asset`
22. Verifikasi `Alert` Warning tampil di atas form
23. Klik row action `Detail` pada baris aset pertama
24. Verifikasi Asset labels tidak lagi memuat `Label Arsip {runId}`

### Asset Label yang dihapus dilepas dari draft dengan peringatan
25. Admin menghapus Asset Label `Label Hapus {runId}`
26. Buka Fixed Asset > Assets > Registration > Draft
27. Ketik Search `Gudang Label Hapus {runId}`, tekan Enter
28. Klik row action `Edit` pada baris batch `Gudang Label Hapus {runId}`
29. Klik tab `Asset`
30. Verifikasi `Alert` Warning tampil di atas form
31. Klik row action `Detail` pada baris aset pertama
32. Verifikasi Asset labels tidak lagi memuat `Label Hapus {runId}`

### Asset Label default pada aset Active tidak dapat dilepas
33. Buka Fixed Asset > Assets > Registration > Draft
34. Klik `[+ Register Asset]`
35. Pilih Group `Gudang Label Aktif {runId}`
36. Klik `[+ Asset Name]`
37. Pilih Asset Name `Router Label {runId}`
38. Pilih Brand `Cisco`
39. Pilih Model `ISR 4331`
40. Isi Quantity `1`
41. Klik `[Save draft]`
42. Klik `[Submit]`
43. Klik `[Activate]`
44. Klik tab `Assets`
45. Ketik Search `Router Label {runId}`, tekan Enter
46. Klik row action `Detail` pada baris aset `Router Label {runId}`
47. Verifikasi Asset labels aset memuat `Label Default {runId}`
48. Klik row action `Edit` pada baris aset `Router Label {runId}`
49. Lepas Asset label `Label Default {runId}`[^drift-1]
50. Simpan perubahan aset
51. Klik row action `Detail` pada baris aset `Router Label {runId}`
52. Verifikasi Asset labels aset tetap memuat `Label Default {runId}`

### Asset Label default pada aset Waiting for Approval
53. Buka Fixed Asset > Assets > Registration > Draft
54. Klik `[+ Register Asset]`
55. Pilih Group `Gudang Label Approval {runId}`
56. Klik `[+ Asset Name]`
57. Pilih Asset Name `Router Label {runId}`
58. Pilih Brand `Cisco`
59. Pilih Model `ISR 4331`
60. Isi Quantity `1`
61. Klik `[Save draft]`
62. Klik `[Submit]`
63. Klik `[Submit for Approval]`
64. Buka Approvals > Registration > Active
65. Ketik Search `Gudang Label Approval {runId}`, tekan Enter
66. Klik row action `Review` pada baris pengajuan `Gudang Label Approval {runId}`
67. Klik Name aset pertama
68. Verifikasi Asset labels pada panel aset memuat `Label Default {runId}`

[^drift-1]: Drift PRD vs kontrak komponen. PRD `FAREG-LOGIC-16d`: Asset Label default "tidak dapat dilepas per aset". Kontrak `MultiSelect#3` dan `MultiSelect#8`: setiap chip punya tombol lepas dan tidak ada chip terkunci. Diasersi: kontrak untuk mekanik chip (tombol lepas ada, sehingga langkah melepas Asset label default dilakukan), PRD untuk aturan bisnis (Asset Label default tetap terpasang pada aset).
