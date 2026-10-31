---
id: TC-GS-IMPORT-E2E-121-ai-reference-suggestion-tidak-berlaku-pada-tab-brand-measurement
title: "AI Reference Suggestion: tidak berlaku pada Tab Brand, Measurement, Position, Division, field Dropdown, dan pembaca Read Only"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-319
  - TC-GS-IMPORT-713
  - TC-GS-IMPORT-714
  - TC-GS-IMPORT-715
  - TC-GS-IMPORT-853
  - TC-GS-IMPORT-933
coverage:
  web: automated
---

# AI Reference Suggestion: tidak berlaku pada Tab Brand, Measurement, Position, Division, field Dropdown, dan pembaca Read Only

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Akun ganti akun (TC-GS-IMPORT-853): Import data (Read Only) Client C (Hari Wibowo) `importRead_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD` (disediakan tim FE). Hook `after` mengembalikan sesi ke Total Control Client C.
- Pelaku kedua (TC-GS-IMPORT-853): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` hanya lewat sesi API sebagai pemicu (P-2), password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (disediakan tim FE).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import; sub-tab dipilih di `## Test Steps`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup Client C: Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam` (`Lembur` dan `Piket` belum menjadi opsi). Client C tanpa draft di semua Tab sebelum tiap TC (fixture reset, Kontrak Fixture R1). Division `Gudang` dihapus oleh TC-GS-IMPORT-853 dan dipulihkan (R2).
- Data Dinamis (berkas disediakan tim QA, fixture baru `Fixture.import.berkas`): D-44 `ai-brand-long.csv` (`Brand Name`), `ai-measurement-long.csv` (`Unit Name,Symbol`; Symbol `kg/m2`), `ai-position-long.csv` (`Position Name`), `ai-division-long.csv` (`Division Name`), masing-masing 1 baris dengan nilai sumber 121 karakter sesuai D-41; D-79 `user-login-shift-lembur.csv` (Shift `Lembur`, `lembur `, `Siang`; baris #1 dan #2 `error`, baris #3 `pending`); `user-login-gudang-1.csv` (berkas User Login standar D-45, 1 baris: Siti Rahmawati, Division `Gudang`, Position kosong).
- Kemampuan teknis: mock layanan AI mode normal (D-40, D-41, D-42) dengan pencatat jumlah permintaan yang dapat dibaca QA; fixture reset draft client; sesi API Admin kedua untuk unggah, konfirmasi pemetaan, dan hapus Division; pemulihan Division `Gudang` oleh fixture.
- State global yang diubah: Division `Gudang` (dihapus lalu dipulihkan pada TC-GS-IMPORT-853). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft semua Tab Client C, pulihkan Division `Gudang` bila belum ada, kembalikan sesi ke Total Control Client C.

## Test Steps

### TC-GS-IMPORT-319: Tab Brand tidak memakai AI Reference Suggestion

1. Pilih sub-tab Brand
2. Klik [Upload File] di toolbar dan pilih berkas `ai-brand-long.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi sel Brand Name baris #1 menampilkan badge "AI suggestion: 'Samsung Electronics Indonesia'?"
5. Verifikasi sel Brand Name baris #1 tidak menampilkan badge "Did you mean"
6. Reset draft Brand Client C lewat fixture reset

### TC-GS-IMPORT-713: Tab Measurement tidak memakai AI Reference Suggestion

7. Pilih sub-tab Measurement
8. Klik [Upload File] di toolbar dan pilih berkas `ai-measurement-long.csv`
9. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
10. Verifikasi sel Unit Name baris #1 menampilkan badge "AI suggestion: 'Kilogram per Square Meter'?"
11. Verifikasi sel Unit Name baris #1 tidak menampilkan badge "Did you mean"
12. Reset draft Measurement Client C lewat fixture reset

### TC-GS-IMPORT-714: Tab Position tidak memakai AI Reference Suggestion

13. Pilih sub-tab Position
14. Klik [Upload File] di toolbar dan pilih berkas `ai-position-long.csv`
15. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
16. Verifikasi sel Position Name baris #1 menampilkan badge "AI suggestion: 'Senior Regional Operations Coordinator'?"
17. Verifikasi sel Position Name baris #1 tidak menampilkan badge "Did you mean"
18. Reset draft Position Client C lewat fixture reset

### TC-GS-IMPORT-715: Tab Division tidak memakai AI Reference Suggestion

19. Pilih sub-tab Division
20. Klik [Upload File] di toolbar dan pilih berkas `ai-division-long.csv`
21. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
22. Verifikasi sel Division Name baris #1 menampilkan badge "AI suggestion: 'Corporate Strategy and Business Development'?"
23. Verifikasi sel Division Name baris #1 tidak menampilkan badge "Did you mean"
24. Reset draft Division Client C lewat fixture reset

### TC-GS-IMPORT-933: Sel Custom Field Dropdown tidak ditemukan tidak memiliki saran dan tetap memakai Create Missing Options

25. Pilih sub-tab User Login
26. Catat jumlah permintaan yang diterima mock layanan AI
27. Klik [Upload File] di toolbar dan pilih berkas `user-login-shift-lembur.csv`
28. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
29. Verifikasi baris pesan "Shift: Invalid option" pada Error Summary Callout memuat `[Create Missing Options]`
30. Verifikasi sel Shift baris #1 dan #2 tidak menampilkan badge saran AI maupun `[Accept]`/`[Dismiss]`
31. Verifikasi mock layanan AI tidak menerima permintaan Reference Suggestion untuk sel Shift (jumlah permintaan sama dengan yang dicatat pada langkah 26)
32. Reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-853: Pembaca Read Only memuat Staging Table dengan tulis-balik ditekan tidak meminta saran ke layanan AI

33. Admin kedua Client C (sesi API): unggah berkas `user-login-gudang-1.csv` dan konfirmasi pemetaan hingga baris #1 `pending` tersimpan
34. Admin kedua Client C (sesi API): hapus Division `Gudang` hingga tersimpan
35. Catat jumlah permintaan yang diterima mock layanan AI
36. Ganti akun: Logout, lalu login sebagai Import data (Read Only) Client C dengan `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD`
37. Buka Import > User Login
38. Verifikasi baris #1 tampil `error` dengan pesan Division not found
39. Verifikasi sel Division baris #1 tidak menampilkan badge saran AI
40. Catat kembali jumlah permintaan yang diterima mock layanan AI
41. Verifikasi jumlah permintaan mock sama dengan jumlah pada langkah 35 (tidak ada permintaan baru)
42. Admin kedua Client C (sesi API): pulihkan Division `Gudang` dan reset draft User Login Client C hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan: empat TC per Tab, TC-GS-IMPORT-933, lalu TC-GS-IMPORT-853 di akhir karena ganti akun dan menghapus Division (aksi merusak ditaruh terakhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 13, 19, 25 (memilih sub-tab), 6, 12, 18, 24, 32, 42 (reset draft dan pemulihan state, S-09), 26, 35, 40 (mencatat jumlah permintaan mock), 33 dan 34 (pemicu Admin kedua), 36 (ganti akun eksplisit, S-07), 37 (membuka halaman).
- P-2: Admin kedua Client C hanya memicu unggah dan penghapusan Division lewat sesi API pada TC-GS-IMPORT-853; hasil yang diasersi ada di sesi Import data (Read Only).
- Asersi absence badge "Did you mean" (langkah 5, 11, 17, 23) berjangkar pada badge "AI suggestion" di sel yang sama; langkah 30 dan 39 berjangkar pada baris pesan atau status `error` yang tampil sebelumnya.
- Langkah 26 mencatat baseline permintaan mock sebelum unggah supaya langkah 31 mencakup seluruh permintaan sejak upload; pada TC sumber pencatatan dilakukan setelah `[Confirm Mapping]`.
- Spec melewati sekitar 35 langkah (42 langkah): enam blok pendek, berdiri sendiri, satu kelas (mock AI sebagai pengamatan tanpa saran), tiap blok mereset draft sendiri.
- Pembagian TC lintas spec: TC-GS-IMPORT-318, 320, 716, 826, 827 (Reference Suggestion berlaku) ada di spec 120; Create Missing Options ada di spec 129 dan 130.
- Temuan untuk QA:
  - TC-GS-IMPORT-933: Expected b ("tidak menerima permintaan Reference Suggestion untuk sel Shift") membandingkan dengan jumlah yang dicatat pada langkah 3 TC, yaitu sesudah Confirm Mapping; permintaan yang terjadi saat Confirm Mapping tidak tercakup. Spec memindahkan pencatatan ke sebelum upload.
  - TC-GS-IMPORT-933: klausa "sebagai satu-satunya jalur pemulihan selain penyuntingan sel" tidak punya asersi yang dapat diamati terpisah; spec hanya memverifikasi `[Create Missing Options]` pada baris pesan.
  - TC-GS-IMPORT-853: pesan "not-found Division" pada Expected a tidak menyebut teks UI persis; spec memakai "Division not found" dari TC Create Missing lain.
  - TC-GS-IMPORT-853: Division `Gudang` adalah data Pre-setup bersama (S-06) dan dihapus oleh TC; atribut aslinya (Code) tidak tercatat di Pre-setup sehingga pemulihan bergantung pada fixture.
  - TC-GS-IMPORT-853: langkah 1-2 TC ("lewat fixture permintaan") tidak menyebut mekanisme unggah dan konfirmasi pemetaan lewat sesi API; disediakan tim FE/BE tanpa endpoint karangan.
  - Berkas `ai-*-long.csv` dari D-44 memuat nilai 121 karakter sesuai D-41, tetapi `user-login-gudang-1.csv` hanya didefinisikan pada kolom Data Uji TC.
  - Post Condition TC-GS-IMPORT-319, 713, 714, 715, 853, dan 933 (isi draft) tidak punya langkah observasi dan tidak diasersi.
