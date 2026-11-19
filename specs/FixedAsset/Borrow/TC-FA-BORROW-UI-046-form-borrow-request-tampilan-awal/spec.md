---
id: TC-FA-BORROW-UI-046-form-borrow-request-tampilan-awal
title: "Form Borrow Request menampilkan field, alert Borrower Overdue, teks bantu Draft, dan aksesibilitas saat pertama tampil"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-01", "FI-BRW-02", "FI-BRW-03", "FI-BRW-53", "FI-BRW-54", "FLD-BRW-01", "§4.2#p4", "§9.9#p2", "§9.9#p3", "§9.9#p13", "EB-FRM-7@form-borrow-request"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-01": [3, 6]
  "FI-BRW-02": 9
  "FI-BRW-03": 10
  "FI-BRW-53": [34, 52]
  "FI-BRW-54": [35, 38]
  "FLD-BRW-01": [23, 26, 29, 32]
  "§4.2#p4": 2
  "§9.9#p2": 12
  "§9.9#p3": [7, 8]
  "§9.9#p13": [13, 14, 16, 55]
  "EB-FRM-7@form-borrow-request": [40, 42, 43, 45, 47, 49]
anchor: [5, 11, 21, 37, 51]
coverage:
  web: automated
---
# Form Borrow Request menampilkan field, alert Borrower Overdue, teks bantu Draft, dan aksesibilitas saat pertama tampil

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request.
- Komponen: Form Borrow Request
- Data:
  - DU-046-1: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Max Duration `3 days`, satuan Duration `days`, Duration dan Purpose kosong.
  - DU-046-2: Aset `Camera Sony A7 IV - 1`, Asset ID `CAM-2026-0001`, Group `Head Office`, Max Duration `4 hours`, satuan Duration `hours`, Duration dan Purpose kosong.
  - DU-046-3: Karyawan `Dewi Lestari`, Position `Staff`, Division `Operations`, sudah tidak aktif.
  - DU-046-4: Karyawan `Wawan`, Position `Operator`, Division `Warehouse`, aktif, tanpa akun login dan tanpa PIC.
  - DU-046-5: Karyawan `Andi Pratama`, Position `Operator`, Division `Warehouse`, aktif, punya satu baris Overdue untuk aset `Projector Epson EB-X06 - 14` dengan Asset Code `PRJ-2026-0014`. Teks alert yang diharapkan `Andi Pratama has an overdue borrow: PRJ-2026-0014.`, dari Name `Andi Pratama` dan Asset Code `PRJ-2026-0014`.
  - DU-046-6: Karyawan `Sari Dewi`, Position `Analyst`, Division `Finance`, aktif, tanpa baris Overdue.
  - DU-046-7: Karyawan `Budi Setiawan`, Position `Staff`, Division `Finance`, aktif, Eligibility `Can borrow`, kandidat di dialog Select Borrower.
  - DU-046-8: Isian Duration `2` untuk baris DU-046-1.
- Kondisi:
  - K1: form Borrow Request baru, Borrower belum dipilih, berisi baris aset DU-046-1 dan DU-046-2; dialog Select Borrower memuat DU-046-7.
  - K2: Draft dibuka dengan Borrower DU-046-3; simpan Draft ditolak karena Borrower sudah tidak aktif.
  - K3: form dengan Borrower DU-046-4; simpan Draft ditolak karena Borrower tidak punya akun login dan tidak punya PIC.
  - K4: halaman Handover untuk transaksi dengan Borrower DU-046-5; Block new borrow when overdue bernilai ON.
  - K5: halaman Handover untuk transaksi dengan Borrower DU-046-6; Block new borrow when overdue bernilai ON.
  - K6: halaman Handover untuk transaksi dengan Borrower DU-046-5; Block new borrow when overdue bernilai OFF.

## Test Steps

### Form baru memuat satu Borrower, isian per aset, dan Note
1. Tampilkan Form Borrow Request dengan kondisi K1
2. Verifikasi judul `Borrow Request` tampil pada form
3. Verifikasi tombol `[Select Borrower]` tampil dan form hanya memiliki satu pemilih Borrower
4. Isi Duration baris `Laptop Dell Latitude 5420 - 10` dengan `2`
5. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` berisi `2`
6. Verifikasi Duration baris `Camera Sony A7 IV - 1` tetap kosong karena Duration diisi per aset
7. Verifikasi setiap baris aset memuat input Duration dan input Purpose
8. Verifikasi field Note tampil pada form yang sama
9. Verifikasi form tidak memiliki isian tanggal
10. Verifikasi form tidak memiliki isian Start date maupun Due date karena masa pinjam dimulai saat handover
11. Verifikasi tombol `[Submit]` tampil
12. Verifikasi tombol `[Borrow Now]` tidak tampil karena hanya milik form Borrow an Asset
13. Verifikasi placeholder `Enter note` tampil pada field Note
14. Verifikasi placeholder `Enter duration` tampil pada Duration baris `Camera Sony A7 IV - 1`
15. Klik ikon Search pada toolbar aset
16. Verifikasi placeholder `Search asset name or ID...` tampil pada kotak Search tabel aset

### Borrower aktif dapat dipilih lewat dialog Select Borrower
17. Tampilkan Form Borrow Request dengan kondisi K1
18. Klik `[Select Borrower]`
19. Pilih baris `Budi Setiawan` pada dialog Select Borrower
20. Klik tombol konfirmasi pada dialog Select Borrower
21. Verifikasi nama `Budi Setiawan` tampil sebagai Borrower pada form
22. Klik `[Save Draft]`
23. Verifikasi caption `You must pick a borrower` tidak tampil pada field Borrower

### Borrower wajib dipilih saat Save Draft
24. Tampilkan Form Borrow Request dengan kondisi K1
25. Klik `[Save Draft]`
26. Verifikasi caption `You must pick a borrower` tampil pada field Borrower

### Borrower yang sudah tidak aktif ditolak saat Save Draft
27. Tampilkan Form Borrow Request dengan kondisi K2
28. Klik `[Save Draft]`
29. Verifikasi caption `Dewi Lestari is no longer active. Pick another borrower.` tampil pada field Borrower

### Borrower tanpa akun login dan tanpa PIC ditolak saat Save Draft
30. Tampilkan Form Borrow Request dengan kondisi K3
31. Klik `[Save Draft]`
32. Verifikasi caption `Wawan has no login account and no PIC. Set a PIC in Users first.` tampil pada field Borrower

### Alert Borrower Overdue tampil di halaman Handover
33. Tampilkan halaman Handover dengan kondisi K4
34. Verifikasi alert `Andi Pratama has an overdue borrow: PRJ-2026-0014.` tampil pada halaman Handover
35. Verifikasi tombol `[Request Confirmation]` tidak disabled sehingga alert tidak memblokir Handover

### Alert Borrower Overdue hilang bila tidak ada baris Overdue
36. Tampilkan halaman Handover dengan kondisi K5
37. Verifikasi tombol `[Request Confirmation]` tampil
38. Verifikasi alert Borrower Overdue tidak tampil pada halaman Handover

### Aksesibilitas field wajib, pesan error, kontrol ikon, dan fokus dialog
39. Tampilkan Form Borrow Request dengan kondisi K1
40. Verifikasi field Borrower, Duration, dan Purpose ditandai wajib (aria-required)
41. Klik `[Save Draft]`
42. Verifikasi pesan error field Borrower terhubung sebagai deskripsi field itu (aria-describedby)
43. Verifikasi tombol ikon `⋯` pada baris `Laptop Dell Latitude 5420 - 10` memiliki label aksesibel `Action`
44. Klik `[Select Borrower]`
45. Verifikasi fokus masuk ke dialog Select Borrower
46. Tekan Tab tiga puluh kali
47. Verifikasi fokus tetap berada di dalam dialog Select Borrower
48. Tekan Esc
49. Verifikasi dialog Select Borrower tertutup dan fokus kembali ke tombol `[Select Borrower]`

### Alert Borrower Overdue tidak tampil bila Block new borrow when overdue OFF
50. Tampilkan halaman Handover dengan kondisi K6
51. Verifikasi tombol `[Request Confirmation]` tampil
52. Verifikasi alert Borrower Overdue tidak tampil pada halaman Handover walaupun Borrower punya baris Overdue

### Placeholder Search pada halaman Handover
53. Tampilkan halaman Handover dengan kondisi K4
54. Klik ikon Search pada toolbar halaman Handover
55. Verifikasi placeholder `Search asset name or ID...` tampil pada kotak Search halaman Handover
