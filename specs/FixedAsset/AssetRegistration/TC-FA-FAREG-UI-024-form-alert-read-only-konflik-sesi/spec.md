---
id: TC-FA-FAREG-UI-024-form-alert-read-only-konflik-sesi
title: "Form Register Asset: Alert, mode read-only, dan dialog konflik sesi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-REG-16", "D-REG-22", "S-REG-19", "S-REG-20", "S-REG-21", "S-REG-26", "S-REG-27", "V-REG-04", "§4.1#r17", "§4.2.1#b1", "§4.2.1#b2", "§4.2.1#b3"]
smoke: []
dependsOn: []
trace:
  "D-REG-16": [33, 34, 36]
  "D-REG-22": [15, 16, 23, 24]
  "S-REG-19": [2, 3]
  "S-REG-20": 7
  "S-REG-21": [9, 10, 13]
  "S-REG-26": [18, 19, 20, 26, 27]
  "S-REG-27": [29, 30]
  "V-REG-04": [2, 5, 40]
  "§4.1#r17": [15, 16]
  "§4.2.1#b1": [2, 3]
  "§4.2.1#b2": 7
  "§4.2.1#b3": [9, 13]
anchor: [12]
coverage:
  web: automated
---

# Form Register Asset: Alert, mode read-only, dan dialog konflik sesi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-024-1: Item `Laptop Dell Latitude 5440` dengan Brand `Dell`, Model `Latitude 5440`, Quantity `3`.
  - DU-024-2: master Brand `Dell` berstatus diarsipkan; pesan `Dell is not available. Choose another Brand.`
  - DU-024-3: alasan approver `Revisi Quantity Laptop Dell`.
  - DU-024-4: Item `Laptop Dell Latitude 5440` dengan Quantity `120`.
  - DU-024-5: pemegang kunci sesi `Rina W`.
  - DU-024-6: pengambil alih kunci sesi `Budi S`.
  - DU-024-7: pengaju yang sudah men-submit draft `Siti N`.
  - DU-024-8: Quantity `121` diketik pada Item `Laptop Dell Latitude 5440`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-024-1; master Brand DU-024-2.
  - K2: form `Edit` draft tersimpan dengan Item DU-024-1; draft dikembalikan approver (`Return to Draft`) dengan alasan DU-024-3.
  - K3: Register Asset Bulk Limit bernilai `100`; form `Edit` draft tersimpan dengan Item DU-024-4.
  - K4: draft tersimpan dengan Item DU-024-1 dibuka untuk diedit saat kunci sesi dipegang DU-024-5.
  - K5: draft tersimpan dengan Item DU-024-1 dibuka lewat row action `Detail`.
  - K6: form `Edit` draft tersimpan dengan Item DU-024-1 sedang dibuka; kunci sesinya direbut DU-024-6 lewat Take over.
  - K7: form `Edit` draft tersimpan dengan Item DU-024-1; draft sudah di-submit oleh DU-024-7 sehingga simpan draft ditolak.
  - K8: form `Edit` draft tersimpan dengan Item DU-024-1 yang Brand `Dell`-nya masih tersedia saat form dibuka; Approval Workflow nonaktif; master Brand diarsipkan sesudah form dibuka (DU-024-2) sehingga Activate ditolak dengan pesan DU-024-2.

## Test Steps
### Alert Warning untuk referensi master yang diarsipkan
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi Alert Warning `Dell is not available. Choose another Brand.` tampil
3. Verifikasi Alert Warning berada di atas form
4. Klik `[Save draft]`
5. Verifikasi pesan `Dell is not available. Choose another Brand.` masih tampil sesudah Save draft

### Alert Danger berisi alasan approver pada draft yang dikembalikan
6. Tampilkan Halaman `Register Asset` dengan kondisi K2
7. Verifikasi Alert Danger memuat alasan `Revisi Quantity Laptop Dell`

### Alert Warning untuk draft di atas Register Asset Bulk Limit baru
8. Tampilkan Halaman `Register Asset` dengan kondisi K3
9. Verifikasi Alert Warning `For more than 100 assets, use Import.` tampil di atas form
10. Verifikasi Alert Warning memuat tautan ke Import
11. Ganti isi sel `Quantity` Item pertama dengan `121`
12. Verifikasi pesan inline `For more than 100 assets, use Import.` tampil di bawah sel `Quantity`
13. Verifikasi Alert Warning tidak tampil bersamaan dengan pesan inline pada sel `Quantity`

### Dialog Draft Is Being Edited dan mode View only
14. Tampilkan Halaman `Register Asset` dengan kondisi K4
15. Verifikasi dialog `Draft Is Being Edited` tampil dengan teks `Rina W is editing this draft. If you take over, their unsaved changes will be lost. Do you want to take over?`
16. Verifikasi dialog memuat tombol `[View only]` dan `[Take over]`
17. Klik `[View only]`
18. Verifikasi footer form memuat `[Close]`
19. Verifikasi form tidak memuat `[Save draft]` dan `[Submit]`
20. Verifikasi isi tabel Item tampil sebagai teks statis tanpa kontrol input
21. Tampilkan Halaman `Register Asset` dengan kondisi K4
22. Tekan `Esc`
23. Verifikasi footer form memuat `[Close]` setelah `Esc`
24. Verifikasi dialog `Draft Is Being Edited` tertutup dan form tampil read-only

### Mode read-only dari row action Detail
25. Tampilkan Halaman `Register Asset` dengan kondisi K5
26. Verifikasi footer form memuat `[Close]`
27. Verifikasi form tidak memuat `[Save draft]` dan `[Submit]` pada mode read-only dari `Detail`

### Pemegang lama melihat Alert dan mode read-only sesudah sesi direbut
28. Tampilkan Halaman `Register Asset` dengan kondisi K6
29. Verifikasi Alert Warning `Your edit session was taken over by Budi S.` tampil
30. Verifikasi form pemegang lama tampil read-only tanpa `[Save draft]` dan `[Submit]`

### Draft yang sudah di-submit orang lain memblok simpan
31. Tampilkan Halaman `Register Asset` dengan kondisi K7
32. Klik `[Save draft]`
33. Verifikasi dialog blok `Draft Already Submitted` tampil dengan teks `This draft was submitted by Siti N. Your changes cannot be saved.`
34. Verifikasi dialog hanya memuat tombol `[OK]`
35. Klik `[OK]`
36. Verifikasi dialog `Draft Already Submitted` tertutup

### Referensi master yang diarsipkan memblok Activate
37. Tampilkan Halaman `Register Asset` dengan kondisi K8
38. Klik `[Submit]`
39. Klik `[Activate]` pada dialog konfirmasi `Activate Assets`
40. Verifikasi pesan `Dell is not available. Choose another Brand.` tampil sesudah `[Activate]`
