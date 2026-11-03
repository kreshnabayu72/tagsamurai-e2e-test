---
id: TC-FA-CF-E2E-125-log-delete-dan-bulk-delete
title: "Log Tiga Surface: Delete dan Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-494
  - TC-FA-CF-495
  - TC-FA-CF-496
coverage:
  web: automated
---

# Log Tiga Surface: Delete dan Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun pelaku sesi 2 (Pre-setup #10 dan #28): Total Control sesi 2 Company Alpha, pengguna Rina Putri (Modified By `Rina P`) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`. Dipakai dua cara: sesi API (login API dengan `Spectra.env.FA_TC2_PASSWORD`, token tidak dihitung sebagai sesi web) untuk menghapus `Compliance File`, dan login UI sesudah semua aksi untuk membaca System Log `Rina Putri` (ganti akun eksplisit pada langkah 49).
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Field yang dihapus: `Legacy Tag` dan `Compliance File`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; jumlah baris hasil Search nama field Pre-setup (`Legacy Tag`, `Compliance File`) pada ketiga surface tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline sebelum aksi (S-12); Search nama field juga tersedia pada System Log `Rina Putri`. Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Langkah 13 dan 29 memulihkan field yang dihapus.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-494: Delete satu field mencatat baris Name di tiga surface

1. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Legacy Tag` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
2. Klik `⋯` > `Delete` pada baris `Legacy Tag`, lalu klik `[Delete]` pada dialog
3. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
4. Buka Modal Changelog tab General, ketik Search `Legacy Tag`, tekan Enter
5. Verifikasi Changelog memuat satu baris dengan Action `Delete`, Field Name `Legacy Tag`, Field `Name`, Old Value `Legacy Tag`, New Value `—`, Modified By `Sarah J`
6. Verifikasi hasil Search `Legacy Tag` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
7. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Legacy Tag`, tekan Enter
8. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Delete`, Object `Custom Fields`, Name `Legacy Tag`, Field `Name`, Old Value `Legacy Tag`, New Value `—`
9. Verifikasi hasil Search `Legacy Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)
10. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Legacy Tag`, tekan Enter
11. Verifikasi Activity Log memuat satu baris dengan Action `Delete`, Object `Custom Fields`, Name `Legacy Tag`, Field `Name`, Old Value `Legacy Tag`, New Value `—`, Modified By `Sarah J`
12. Verifikasi hasil Search `Legacy Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda dan tidak ada baris untuk properti yang tidak berubah)

### TC-FA-CF-495: Bulk Delete dua field mencatat Action Bulk Delete satu entri per field

13. Pulihkan baseline Company lewat seed reset Company (`Legacy Tag` dan `Compliance File` ada kembali) lalu muat ulang tabel
14. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Legacy Tag` lalu `Compliance File` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
15. Centang baris `Legacy Tag` dan `Compliance File`, lalu hapus lewat Bulk Action Bar dan konfirmasi dialog Bulk Delete
16. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
17. Buka Modal Changelog tab General, ketik Search `Legacy Tag`, tekan Enter
18. Verifikasi hasil Search `Legacy Tag` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Legacy Tag` dengan Field `Name`, Old Value `Legacy Tag`, dan New Value `—`, bukan Action `Delete`)
19. Ganti isi kotak search dengan `Compliance File`, tekan Enter
20. Verifikasi hasil Search `Compliance File` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Compliance File` dengan Field `Name`, Old Value `Compliance File`, dan New Value `—`, bukan Action `Delete`)
21. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Legacy Tag`, tekan Enter
22. Verifikasi hasil Search `Legacy Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Legacy Tag` dengan Field `Name`, Old Value `Legacy Tag`, dan New Value `—`, bukan Action `Delete`)
23. Ganti isi kotak search dengan `Compliance File`, tekan Enter
24. Verifikasi hasil Search `Compliance File` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Compliance File` dengan Field `Name`, Old Value `Compliance File`, dan New Value `—`, bukan Action `Delete`)
25. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Legacy Tag`, tekan Enter
26. Verifikasi hasil Search `Legacy Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Legacy Tag` dengan Field `Name`, Old Value `Legacy Tag`, dan New Value `—`, bukan Action `Delete`)
27. Ganti isi kotak search dengan `Compliance File`, tekan Enter
28. Verifikasi hasil Search `Compliance File` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Bulk Delete` untuk `Compliance File` dengan Field `Name`, Old Value `Compliance File`, dan New Value `—`, bukan Action `Delete`)

### TC-FA-CF-496: Bulk Delete yang hanya menghapus satu field mencatat Action Delete

29. Pulihkan baseline Company lewat seed reset Company (`Legacy Tag` dan `Compliance File` ada kembali) lalu muat ulang tabel
30. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log, serta System Log `Rina Putri` (Settings > User > Detail pengguna `Rina Putri` > Tab System Log), ketik Search `Legacy Tag` lalu `Compliance File` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
31. Centang baris `Legacy Tag` dan `Compliance File`
32. Klik Bulk Delete pada Bulk Action Bar sampai dialog konfirmasi Bulk Delete tampil
33. Dari sesi 2 (`Rina Putri`, sesi API) hapus `Compliance File` hingga tersimpan
34. Konfirmasi dialog Bulk Delete di sesi 1
35. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
36. Buka Modal Changelog tab General, ketik Search `Legacy Tag`, tekan Enter
37. Verifikasi hasil Search `Legacy Tag` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete`, Field Name `Legacy Tag`, Field `Name`, Old Value `Legacy Tag`, New Value `—`, Modified By `Sarah J`)
38. Ganti isi kotak search dengan `Compliance File`, tekan Enter
39. Verifikasi hasil Search `Compliance File` pada Changelog bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete`, Field Name `Compliance File`, Field `Name`, Old Value `Compliance File`, New Value `—`, Modified By `Rina P`, milik sesi 2)
40. Verifikasi hasil Search `Compliance File` pada Changelog tidak memuat baris baru dengan Modified By `Sarah J` (aksi sesi 1 tidak menulis entri untuk field yang dilewati; satu-satunya baris baru milik sesi 2)
41. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Legacy Tag`, tekan Enter
42. Verifikasi hasil Search `Legacy Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete` untuk `Legacy Tag` dengan Modified By `Sarah J`)
43. Ganti isi kotak search dengan `Compliance File`, tekan Enter
44. Verifikasi hasil Search `Compliance File` pada Activity Log bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete` untuk `Compliance File` dari sesi 2 dengan Modified By `Rina P`)
45. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Legacy Tag`, tekan Enter
46. Verifikasi hasil Search `Legacy Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete` untuk `Legacy Tag`)
47. Ganti isi kotak search dengan `Compliance File`, tekan Enter
48. Verifikasi hasil Search `Compliance File` pada System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru Delete `Compliance File` pada System Log `Sarah Johnson`)
49. Ganti akun: logout dari sesi 1, lalu login sebagai Total Control sesi 2 `Rina Putri` (Pre-setup #10)
50. Buka Settings > User > Detail pengguna `Rina Putri` > Tab System Log, ketik Search `Compliance File`, tekan Enter
51. Verifikasi hasil Search `Compliance File` pada System Log `Rina Putri` bertambah tepat satu baris dibanding baseline (satu baris baru Action `Delete` untuk `Compliance File`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 51 langkah bernomor; langkah blok baca-log berpola (buka surface dengan Search nama field, `Verifikasi` selisih jumlah baris hasil Search; 36 langkah, nomor 4 sampai 12, 17 sampai 28, 36 sampai 48, 50 sampai 51) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 15 langkah. Spec dipertahankan karena semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna.
- Urutan TC di spec: 494, 495, 496. Setiap TC menghapus field baseline; langkah 13 dan 29 memulihkannya (S-09). TC-FA-CF-496 berada di akhir karena berakhir dengan ganti akun ke sesi 2.
- Sesi 2 hanya memicu perubahan state lewat sesi API (bukan konteks kedua kelas c); langkah penghapusan sesi 2 ditulis "... hingga ... tersimpan" (R-20). Login UI sesi 2 sesudah semua aksi sesi 1 dipakai berurutan, sehingga satu sesi web aktif pada satu waktu; hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, 29, baseline di awal tiap TC, "Tunggu aksi selesai" sebelum membuka surface log (8b butir 8), langkah buka surface log dengan Search nama field, dan ganti isi kotak search (R-16).
- Nama field Pre-setup (`Legacy Tag`, `Compliance File`) tidak unik pada audit trail permanen. "Satu baris", "dua baris", dan "tidak ada baris" TC-FA-CF-494, 495, dan 496 ditulis sebagai selisih jumlah baris hasil Search nama field terhadap baseline sebelum aksi pada surface yang sama (S-12), bukan sebagai jumlah absolut; baris yang diasersi sebagai selisih adalah baris Action yang ditulis di `Verifikasi`.
- TC-FA-CF-495 butir b ("tidak ada baris dengan Action `Delete`") dipenuhi karena selisih satu baris per field di setiap surface sepenuhnya baris Action `Bulk Delete` (bukan `Delete`); tidak ada `Verifikasi` absence terpisah.
- Absence "tidak ada entri baru" untuk aksi sesi 1 pada `Compliance File` (TC-FA-CF-496) beranchor baris positif milik sesi 2 pada Changelog (selisih satu baris Modified By `Rina P`) dan pada System Log `Sarah Johnson` beranchor baris positif `Legacy Tag` pada surface yang sama (8b butir 2).
- Temuan untuk QA:
  - TC-FA-CF-496 tidak menyatakan kapan dialog Bulk Delete dibuka relatif terhadap penghapusan sesi 2; spec membuka dialog lebih dulu, lalu sesi 2 menghapus, lalu konfirmasi (urutan TC, S-04).
  - TC-FA-CF-495 dan TC-FA-CF-496 tidak menyebut label tombol konfirmasi Bulk Delete; spec menulis "konfirmasi dialog Bulk Delete".
  - Email akun Total Control sesi 2 Company Alpha mengikuti pola Pre-setup #10; env var `FA_TC2_PASSWORD` disediakan tim FE.
