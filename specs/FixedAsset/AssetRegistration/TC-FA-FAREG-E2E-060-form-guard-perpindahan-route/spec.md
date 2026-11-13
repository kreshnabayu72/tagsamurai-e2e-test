---
id: TC-FA-FAREG-E2E-060-form-guard-perpindahan-route
title: "Form Register Asset: dialog Unsaved Changes saat berpindah route"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-REG-15, FAREG-LOGIC-20a, EB-FRM-2@form-register-asset]
smoke: []
dependsOn: []
trace:
  D-REG-15: [4, 5, 6]
  FAREG-LOGIC-20a: [4, 8, 10, 13, 17, 26, 44, 45, 46]
  EB-FRM-2@form-register-asset: [4, 13, 21, 30, 32, 33]
anchor: [16, 25, 37]
coverage:
  web: automated
---

# Form Register Asset: dialog Unsaved Changes saat berpindah route

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Guard {runId}`, `Gudang Guard Pembanding {runId}`, `Gudang Guard Esc {runId}`, dan `Gudang Guard Submit {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-060-1: Group `Gudang Guard {runId}`, node Assignable dan bukan Excess, belum memiliki batch Draft.
  - DU-060-4: Group `Gudang Guard Esc {runId}`, node Assignable dan bukan Excess, belum memiliki batch Draft.
  - DU-060-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Guard Pembanding {runId}`, berisi satu Item `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`.
  - DU-060-5: Draft tersimpan milik `Rina W` untuk Group `Gudang Guard Submit {runId}`, berisi satu Item `Office Desk`, `Kayu Jati`, `No Model` dengan Quantity `1`, Condition `Normal`, TAG Type `Non-TAG`; Total Asset `1`; aset memenuhi Tingkat 2 dan belum memiliki Alias Name.
- Kondisi:
  - Group `Gudang Guard Submit {runId}` ber-toggle `Require Approval for Registration` OFF.

## Test Steps

### Pindah menu sidebar dengan form kotor membuka dialog Unsaved Changes
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Guard {runId}`
3. Klik item `Assets` pada sidebar
4. Verifikasi dialog `Unsaved Changes` tampil
5. Verifikasi isi dialog `You have unsaved changes. Are you sure you want to leave?`
6. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
7. Klik `[Cancel]`
8. Verifikasi form Register Asset tetap terbuka dengan Group `Gudang Guard {runId}` masih terpilih

### Klik breadcrumb dengan form kotor membuka dialog yang sama
9. Klik breadcrumb `Draft`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Cancel]`

### Tombol Back browser dengan form kotor menutup form tanpa menyimpan setelah Leave
12. Klik tombol Back browser
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi baris Group `Gudang Guard Pembanding {runId}` tampil di sub tab Draft
17. Verifikasi baris Group `Gudang Guard {runId}` tidak tampil karena form ditutup tanpa menyimpan

### Muat ulang halaman dengan form kotor memunculkan konfirmasi bawaan browser
18. Klik `[+ Register Asset]`
19. Pilih Group `Gudang Guard {runId}`
20. Muat ulang halaman
21. Verifikasi konfirmasi bawaan browser muncul karena form kotor
22. Batalkan konfirmasi bawaan browser sehingga tetap berada di form

### Guard dilepas setelah Save draft
23. Klik `[Save draft]`
24. Klik breadcrumb `Draft`
25. Verifikasi sub tab `Draft` tampil
26. Verifikasi dialog `Unsaved Changes` tidak tampil

### Esc pada dialog Unsaved Changes sama dengan Cancel
27. Klik `[+ Register Asset]`
28. Pilih Group `Gudang Guard Esc {runId}`
29. Klik breadcrumb `Draft`
30. Verifikasi dialog `Unsaved Changes` tampil
31. Tekan `Esc`
32. Verifikasi form Register Asset tetap terbuka dengan Group `Gudang Guard Esc {runId}` masih terpilih
33. Verifikasi dialog `Unsaved Changes` tertutup
34. Klik breadcrumb `Draft`
35. Klik `[Leave]` pada dialog Unsaved Changes

### Guard dilepas setelah Submit berhasil
36. Ketik Search `Gudang Guard Submit {runId}`, tekan Enter
37. Verifikasi baris Group `Gudang Guard Submit {runId}` tampil di tabel Draft
38. Klik ikon `Edit` pada baris Group `Gudang Guard Submit {runId}`
39. Klik tab `Asset`
40. Klik row option `Detail` pada aset 1
41. Isi Alias Name `Meja Direksi` pada panel samping aset
42. Klik `[Submit]`
43. Klik `[Activate]` pada dialog konfirmasi
44. Verifikasi toast `Success, asset has been activated.` tampil
45. Verifikasi halaman kembali ke Registration dengan sub tab `History` aktif
46. Verifikasi dialog `Unsaved Changes` tidak tampil
