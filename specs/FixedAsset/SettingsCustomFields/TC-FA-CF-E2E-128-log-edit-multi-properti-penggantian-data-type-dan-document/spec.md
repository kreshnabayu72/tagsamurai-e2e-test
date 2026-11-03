---
id: TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document
title: "Log Tiga Surface: Multi-Properti, Penggantian Data Type, Opsi, dan Document"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-499
  - TC-FA-CF-500
  - TC-FA-CF-501
  - TC-FA-CF-502
  - TC-FA-CF-647
coverage:
  web: automated
---

# Log Tiga Surface: Multi-Properti, Penggantian Data Type, Opsi, dan Document

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12, Max custom fields per asset name 20) dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diedit: `Required Check` (Text, Required No, Placeholder `Fill me`, tanpa nilai), `Voltage Spec` (Text, Global), `Storage Capacity`, `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`; A1 = `Gold`), dan `Global Doc File` (Document, Global, berkas `original.pdf`). Berkas uji `replacement.pdf` (Pre-setup #36) dirujuk lewat fixture `Fixture.faCustomFields.berkas`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-501: Penggantian Data Type ke Formula mencatat baris Required, Value Type, dan Placeholder yang ikut berubah

1. Klik row action `⋯` > `Edit` pada baris `Required Check` (Text, Required No, Placeholder `Fill me`), ubah toggle Required ke Yes, lalu klik `[Save]`
2. Klik row action `⋯` > `Edit` pada baris `Required Check`, ganti Data Type menjadi `Formula`, susun `Purchase Price + 1`, lalu klik `[Save]` (tanpa dialog karena field tanpa nilai aset)
3. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
4. Buka Modal Changelog tab General dan temukan baris submit kedua untuk `Required Check`
5. Verifikasi Changelog memuat baris Edit properti `Data Type` dengan Old Value `Text` dan New Value `Formula`
6. Verifikasi Changelog memuat baris Edit properti `Formula` dengan Old Value `—` dan New Value `[Purchase Price] + 1`
7. Verifikasi Changelog memuat baris Edit properti `Required` dengan Old Value `Yes` dan New Value `No` sebagai baris tersendiri
8. Verifikasi Changelog memuat baris Edit properti `Placeholder` dengan Old Value `Fill me` dan New Value `—` sebagai baris tersendiri

### TC-FA-CF-500: Penggantian Data Type mencatat baris Data Type beserta baris properti yang ikut berubah

9. Catat jumlah entri Changelog tab General sebagai baseline
10. Klik row action `⋯` > `Edit` pada baris `Voltage Spec` (Text, Global)
11. Ganti Data Type menjadi `Dropdown` dan tambah opsi `A`
12. Klik `[Save]`
13. Verifikasi dialog `Change Data Type` tampil
14. Verifikasi dialog `Change to Specific Value` tidak tampil karena Value Type kembali ke Specific mengikuti `FACF-LOGIC-11d`
15. Klik `[Change Data Type]` pada dialog
16. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
17. Buka Modal Changelog tab General dan temukan baris `Voltage Spec`
18. Verifikasi Changelog memuat baris Edit `Data Type` dengan Old Value `Text` dan New Value `Dropdown`
19. Verifikasi Changelog memuat baris Edit `Dropdown Options` dengan Old Value `—` dan New Value `A`
20. Verifikasi Changelog memuat baris Edit `Global Value` dengan Old Value `Generator: 220V; Pump: 110V` dan New Value `—`
21. Verifikasi Changelog memuat baris Edit `Value Type` dengan Old Value `Global` dan New Value `Specific`
22. Verifikasi jumlah entri Changelog tab General bertambah tepat empat dibanding baseline (tidak ada baris per aset terdampak)

### TC-FA-CF-499: Edit tiga properti sekaligus menulis satu baris per properti

23. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
24. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
25. Ubah Field Name menjadi `Storage Capacity 2 {runId}-128`, Placeholder menjadi `GB`, dan Required Yes
26. Klik `[Save]`
27. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
28. Buka Modal Changelog tab General dan temukan baris `Storage Capacity 2 {runId}-128`
29. Verifikasi Changelog memuat tiga baris Edit (properti `Name`, `Placeholder`, dan `Required`) dengan waktu submit yang sama
30. Verifikasi jumlah entri Changelog tab General bertambah tepat tiga dibanding baseline (properti yang tidak berubah, mis. Scope dan Data Type, tidak menulis baris)
31. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Storage Capacity 2 {runId}-128`
32. Verifikasi System Log `Sarah Johnson` memuat tiga baris Edit (properti `Name`, `Placeholder`, dan `Required`) dengan waktu submit yang sama
33. Verifikasi jumlah entri System Log `Sarah Johnson` bertambah tepat tiga dibanding baseline (properti yang tidak berubah, mis. Scope dan Data Type, tidak menulis baris)
34. Buka Reports & Logs > Activity Log > Tab User Action dan temukan baris `Storage Capacity 2 {runId}-128`
35. Verifikasi Activity Log memuat tiga baris Edit (properti `Name`, `Placeholder`, dan `Required`) dengan waktu submit yang sama
36. Verifikasi jumlah entri Activity Log bertambah tepat tiga dibanding baseline (properti yang tidak berubah, mis. Scope dan Data Type, tidak menulis baris)

### TC-FA-CF-502: Rename dan hapus opsi Dropdown dicatat sebagai Edit Dropdown Options tanpa entri tambahan

37. Catat jumlah entri Changelog tab General sebagai baseline
38. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
39. Rename opsi `Gold` menjadi `Platinum` dan hapus opsi `Bronze`, lalu konfirmasi `[Remove]`
40. Klik `[Save]`
41. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
42. Buka Modal Changelog tab General dan temukan baris `Brand Tier`
43. Verifikasi Changelog memuat satu baris Edit properti `Dropdown Options` dengan Old Value `Gold, Silver, Bronze` dan New Value `Platinum, Silver` pada submit tersebut
44. Verifikasi jumlah entri Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris tambahan untuk nilai aset yang ter-cascade)

### TC-FA-CF-647: Edit file Global Value Document mencatat nama file Old dan New di tiga surface

45. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Global Doc File` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
46. Klik row action `⋯` > `Edit` pada baris `Global Doc File`
47. Pilih berkas `replacement.pdf` (mengganti `original.pdf`) lalu klik `[Save]`
48. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
49. Buka Modal Changelog tab General, ketik Search `Global Doc File`, tekan Enter
50. Verifikasi Changelog memuat satu baris baru Action `Edit`, Field `Global Value`, Old Value `original.pdf`, dan New Value `replacement.pdf`
51. Verifikasi hasil Search `Global Doc File` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
52. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Global Doc File`, tekan Enter
53. Verifikasi System Log `Sarah Johnson` memuat satu baris baru Action `Edit`, Field `Global Value`, Old Value `original.pdf`, dan New Value `replacement.pdf`
54. Verifikasi hasil Search `Global Doc File` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
55. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Global Doc File`, tekan Enter
56. Verifikasi Activity Log memuat satu baris baru Action `Edit`, Field `Global Value`, Old Value `original.pdf`, dan New Value `replacement.pdf`
57. Verifikasi hasil Search `Global Doc File` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 57 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log dan selisih jumlah per surface; 32 langkah, nomor 4 sampai 8, 17 sampai 22, 28 sampai 36, 42 sampai 44, 49 sampai 57) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 25 langkah. Spec dipertahankan karena semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna.
- Urutan TC di spec: 501, 500, 499, 502, 647; setiap TC mengedit field berbeda sehingga tidak ada ketergantungan state.
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline di awal TC-FA-CF-500, 499, 502, dan 647 (TC-FA-CF-501 tidak memakai baseline jumlah) dan langkah buka serta temukan baris di tiap surface (R-16); langkah 3, 16, 27, 41, dan 48 ("Tunggu aksi selesai" sesudah `[Save]` sebelum Modal Changelog dibuka; 8b butir 8; asersi tambahan di luar Expected TC, S-03). TC-FA-CF-500, 501, dan 502 hanya membaca Modal Changelog karena itu surface yang disebut langkah TC.
- TC-FA-CF-647: "baris baru" ditulis sebagai selisih satu baris pada jumlah baris hasil Search `Global Doc File` terhadap baseline per surface (langkah 45), karena nama field tidak unik pada audit trail permanen (S-12).
- Dialog `Change Data Type` hanya muncul pada TC-FA-CF-500; TC-FA-CF-501 tanpa dialog karena field tanpa nilai aset (sesuai TC).
- Temuan untuk QA:
  - TC-FA-CF-501 Expected b menulis baris Required Old `Yes` New `No`: Required sebelumnya diubah ke Yes pada langkah pertama TC, lalu dikembalikan oleh penggantian Data Type ke Formula; spec mengikuti TC.
  - TC-FA-CF-647 tidak menyebut kolom Modified By, Object, dan Name; spec hanya mengasersi Action, Field, Old Value, dan New Value seperti Expected.
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
