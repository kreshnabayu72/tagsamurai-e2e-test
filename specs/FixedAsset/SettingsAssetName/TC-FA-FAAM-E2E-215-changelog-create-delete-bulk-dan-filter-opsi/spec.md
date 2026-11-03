---
id: TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi
title: "Pencatatan Changelog: Create, Delete, Bulk Delete, dan Jejak Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-572
  - TC-FA-FAAM-573
  - TC-FA-FAAM-574
  - TC-FA-FAAM-583
coverage:
  web: automated
---

# Pencatatan Changelog: Create, Delete, Bulk Delete, dan Jejak Delete

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (dibaca saja, tidak diubah): No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`), No. 25 (Label `Finance`), No. 14o (`Bulk Used X`, Total Asset 3, in-use; hanya ikut dipilih pada Bulk Delete dan dilewati guard, tidak berubah, Last Updated tidak berubah).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-215`:
  - `Log Delete Item {runId}-215`: salinan fixture 13h (Total Asset 0). Sesi API aktor membuat lalu mengubah UoM hingga tersimpan agar Changelog memuat entri Create dan Edit sebelum Delete (TC-FA-FAAM-583 mensyaratkan entri Create dan Edit lama).
  - `Bulk Clean A 574 {runId}-215` dan `Bulk Clean B 574 {runId}-215`: salinan fixture 13c (Tabel Dinamis No. 68), Total Asset 0.
  - Asset Name hasil Create TC-FA-FAAM-572: `Log Create Item {runId}-215` dengan Code `LCI572`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Default Addon `Audit`, Default Label `Finance`. Nilai field TC tidak disebut TC (lihat Temuan untuk QA).
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya; membaca jumlah baris hasil Search Changelog sebelum aksi (baseline). Changelog adalah audit trail permanen sehingga total entri tidak diasersi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Log Create Item {runId}-215` dan sisa seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-572, 573, 574, 583: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan dan baseline

1. Ketik Search `Bulk`, tekan Enter
2. Klik icon Changelog
3. Ketik Search `Bulk Used X`, tekan Enter
4. Catat jumlah baris Changelog `Bulk Used X` sebagai baseline N
5. Tutup Modal Changelog

### TC-FA-FAAM-572: Create mencatat satu baris saja

6. Ganti isi kotak search dengan `{runId}-215`, tekan Enter
7. Klik `[+ Asset Name]`
8. Isi `Log Create Item {runId}-215`, Code `LCI572`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Default Addon `Audit`, Default Label `Finance`
9. Klik `[Submit]`
10. Klik icon Changelog
11. Ketik Search `Log Create Item {runId}-215`, tekan Enter
12. Verifikasi satu baris: Action `Create`, Field `Asset Name`, Old `—`, New `Log Create Item {runId}-215`
13. Verifikasi jumlah baris untuk `Log Create Item {runId}-215` tepat satu (atribut konfigurasi awal lain tidak dicatat per baris)
14. Tutup Modal Changelog

### TC-FA-FAAM-573: Delete mencatat satu baris dengan New strip

15. Klik `⋯` baris `Log Delete Item {runId}-215` lalu `Delete`
16. Klik `[Delete]`
17. Klik icon Changelog
18. Ketik Search `Log Delete Item {runId}-215`, tekan Enter
19. Verifikasi satu baris Action `Delete`, Asset Name `Log Delete Item {runId}-215`, Field `Asset Name`, Old `Log Delete Item {runId}-215`, New `—`

### TC-FA-FAAM-583: Entri log Delete tetap sebagai jejak setelah Asset Name dihapus

20. Verifikasi entri Create, Edit, dan Delete lama `Log Delete Item {runId}-215` tetap tampil apa adanya
21. Tutup Modal Changelog

### TC-FA-FAAM-574: Bulk Delete satu baris per item dengan Date sama

22. Ganti isi kotak search dengan `Bulk`, tekan Enter
23. Centang `Bulk Clean A 574 {runId}-215`, `Bulk Clean B 574 {runId}-215`, dan `Bulk Used X`
24. Klik `Bulk Action` lalu `Delete`
25. Klik `[Continue]`
26. Klik icon Changelog
27. Ketik Search `574 {runId}-215`, tekan Enter
28. Verifikasi dua baris Action `Delete` untuk `Bulk Clean A 574 {runId}-215` dan `Bulk Clean B 574 {runId}-215`
29. Verifikasi kedua baris Delete memiliki Date yang sama persis
30. Ganti isi kotak search dengan `Bulk Used X`, tekan Enter
31. Verifikasi jumlah baris Changelog `Bulk Used X` sama dengan baseline N pada langkah 4
32. Tutup Modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search agar baris Bulk tampil), langkah 3, 11, 18, 27, 30 (Search di Modal Changelog untuk menemukan entri target pada audit trail permanen; S-12, S-14), langkah 5, 14, 21, 32 (menutup Modal Changelog), dan langkah 6 serta 22 (mengganti isi Search tabel utama).
- Pembagian TC lintas spec: TC-FA-FAAM-585 dan TC-FA-FAAM-586 (opsi Filter Field dan Action) ada di spec 239.
- TC-FA-FAAM-583 bergantung pada TC-FA-FAAM-573 (Dependensi); langkah 20 memakai Modal Changelog yang sama setelah langkah 19, dan langkah TC-FA-FAAM-573 dijalankan penuh di spec ini (S-04).
- Langkah 31 menggantikan asersi absence "tidak ada baris untuk `Bulk Used X`" dengan asersi jumlah terhadap baseline; asersi absence murni hanya di spec kelas g (S-05).
- Temuan untuk QA:
  - TC-FA-FAAM-572 tidak menyebut nilai Code, Default Addon, dan Default Label; spec memilih `LCI572`, `Audit`, `Finance` dari Pre-setup. Lisensi `Audit` diasumsikan aktif.
  - TC-FA-FAAM-583 hanya menyebut Asset Name "yang sudah dihapus" tanpa cara entri Create dan Edit lama terbentuk; spec membentuknya lewat sesi API aktor.
  - TC-FA-FAAM-574 menyebut tombol `Continue` tanpa dialog Bulk Delete yang memuatnya; spec mengikuti TC.
  - TC-FA-FAAM-574 butir b ("tidak ada baris untuk `Bulk Used X`") berisi klausa absence log tanpa spec kelas g yang memuat aksi nyata; spec memakai asersi jumlah. Keputusan pemilik: pindahkan ke spec 216 atau terima.
