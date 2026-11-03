---
id: TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log
title: "Log: Snapshot Nama, Sinkron, dan Kepemilikan System Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-506
  - TC-FA-CF-507
  - TC-FA-CF-508
  - TC-FA-CF-509
coverage:
  web: automated
---

# Log: Snapshot Nama, Sinkron, dan Kepemilikan System Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun Total Control sesi 2 Company Alpha, pengguna Rina Putri (Modified By `Rina P`; Pre-setup #10 dan #28) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, dipakai sebagai akun aktor kedua lewat ganti akun eksplisit (login UI dengan `Spectra.env.FA_TC2_PASSWORD`).
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Field yang diedit: `Storage Capacity` (rename dua kali), `Asset Serial Tag` (Required Yes), `Legacy Tag` (Text), dan `Total Cost` (Formula, Active). Hasil rename bersuffix `{runId}-129`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- State global: nama pengguna `Rina Putri` diubah menjadi `Rina Pratama` pada TC-FA-CF-507; hook `after` memulihkan nama pengguna `Rina Putri` dan mengembalikan sesi ke akun default suite.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-506: Entri lama tetap menampilkan nama saat kejadian setelah rename dua kali

1. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`, ubah Field Name menjadi `Storage B {runId}-129`, lalu klik `[Save]`
2. Klik row action `⋯` > `Edit` pada baris `Storage B {runId}-129`, ubah Field Name menjadi `Storage C {runId}-129`, lalu klik `[Save]`
3. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
4. Buka Modal Changelog tab General dan temukan baris yang memuat `{runId}-129`
5. Verifikasi entri rename pertama: Action `Edit`, Field `Name`, Old Value `Storage Capacity`, New Value `Storage B {runId}-129`
6. Verifikasi entri rename kedua: Action `Edit`, Field `Name`, Old Value `Storage B {runId}-129`, New Value `Storage C {runId}-129`
7. Verifikasi kolom Field Name entri rename pertama memuat `Storage B {runId}-129` dan entri rename kedua memuat `Storage C {runId}-129` (nama sesudah perubahan)

### TC-FA-CF-508: Setiap mutasi menulis ke ketiga surface secara sinkron

8. Pada Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log ketik Search `Asset Serial Tag` (satu per satu) dan catat jumlah baris hasil Search masing-masing sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
9. Klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`, ubah toggle Required ke No, klik `[Save]`, lalu segera buka ketiga surface log
10. Buka Modal Changelog tab General, ketik Search `Asset Serial Tag`, tekan Enter
11. Verifikasi Changelog memuat satu baris baru dengan Action `Edit`, Field Name `Asset Serial Tag`, Field `Required`, Old Value `Yes`, New Value `No`, Modified By `Sarah J`
12. Verifikasi hasil Search `Asset Serial Tag` pada Changelog bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
13. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log, ketik Search `Asset Serial Tag`, tekan Enter
14. Verifikasi System Log `Sarah Johnson` memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Asset Serial Tag`, Field `Required`, Old Value `Yes`, New Value `No`
15. Verifikasi hasil Search `Asset Serial Tag` pada System Log `Sarah Johnson` bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
16. Buka Reports & Logs > Activity Log > Tab User Action, ketik Search `Asset Serial Tag`, tekan Enter
17. Verifikasi Activity Log memuat satu baris baru dengan Action `Edit`, Object `Custom Fields`, Name `Asset Serial Tag`, Field `Required`, Old Value `Yes`, New Value `No`, Modified By `Sarah J`
18. Verifikasi hasil Search `Asset Serial Tag` pada Activity Log bertambah tepat satu baris dibanding baseline (tidak ada baris ganda)
19. Verifikasi entri yang sama muncul di Changelog, System Log `Sarah Johnson`, dan Activity Log tanpa selisih (Action, Field, Old Value, dan New Value identik pada ketiga surface)

### TC-FA-CF-509: System Log mencatat aksi dari sisi aktor dan tidak muncul pada pengguna lain

20. Buka Settings > User > Detail pengguna `Rina Putri` > Tab System Log, catat jumlah entri System Log `Rina Putri` sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
21. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`, isi Placeholder `Check {runId}-129`, lalu klik `[Save]` oleh Total Control `Sarah Johnson`
22. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
23. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan temukan baris `Legacy Tag`
24. Verifikasi System Log `Sarah Johnson` memuat satu baris dengan Action `Edit`, Object `Custom Fields`, Name `Legacy Tag`, Field `Placeholder`, Old Value `—`, New Value `Check {runId}-129`
25. Buka Settings > User > Detail pengguna `Rina Putri` > Tab System Log
26. Verifikasi Tab System Log Detail `Rina Putri` tampil dan jumlah entrinya sama dengan baseline
27. Verifikasi System Log `Rina Putri` tidak memuat entri Edit `Legacy Tag`

### TC-FA-CF-507: Modified By dan Name tetap snapshot setelah aktor berubah

28. Ganti akun: logout dari sesi `Sarah Johnson`, lalu login sebagai Total Control sesi 2 `Rina Putri` (Pre-setup #10)
29. Buka Modal Changelog tab General, ketik Search `Total Cost`, tekan Enter, catat jumlah baris hasil Search sebagai baseline, lalu tutup Modal Changelog
30. Geser switch Active baris `Total Cost` ke OFF
31. Klik `[Deactivate]`
32. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
33. Buka Modal Changelog tab General, ketik Search `Total Cost`, tekan Enter, dan temukan entri Deactivate `Total Cost` yang dibuat aktor `Rina Putri`
34. Verifikasi jumlah baris hasil Search `Total Cost` bertambah tepat satu dibanding baseline sebelum Deactivate (satu entri Deactivate baru)
35. Verifikasi entri Deactivate `Total Cost` menampilkan Modified By `Rina P`
36. Catat nilai kolom Date dan jumlah baris hasil Search `Total Cost` pada entri Deactivate `Total Cost` tersebut
37. Tutup Modal Changelog, lalu ubah nama pengguna `Rina Putri` menjadi `Rina Pratama` di Global Settings > User
38. Tunggu aksi selesai (perubahan nama pengguna tersimpan)
39. Buka Modal Changelog tab General di Settings > Custom Fields, ketik Search `Total Cost`, tekan Enter, dan temukan entri Deactivate `Total Cost` yang sama
40. Verifikasi entri tersebut tetap menampilkan Modified By `Rina P`
41. Verifikasi entri lama tetap menampilkan snapshot saat aksi dan tidak ditulis ulang (kolom Date sama dengan yang dicatat pada langkah 36 dan jumlah baris hasil Search `Total Cost` sama dengan jumlah yang dicatat pada langkah 36, selisih terhadap baseline tetap satu entri Deactivate `Total Cost`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 41 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log dan selisih jumlah) membentuk sebagian besar langkah, dan semua blok berada pada satu kelas harness (pencatatan log tiga surface) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok TC lain kehilangan makna. Langkah "Tunggu aksi selesai" dan baseline/selisih TC-FA-CF-507 menambah jumlah langkah.
- TC-FA-CF-508 (langkah 8 sampai 19): "satu baris" ditulis sebagai selisih jumlah baris hasil Search `Asset Serial Tag` terhadap baseline per surface, karena nama field tidak unik pada audit trail permanen (S-12).
- Langkah 9 (TC-FA-CF-508) sengaja langsung membuka ketiga surface log tanpa "Tunggu aksi selesai", karena TC-FA-CF-508 menyatakan "segera buka ketiga surface" dan Expected "tanpa selisih" menguji sinkronisasi segera.
- Urutan TC di spec: 506, 508, 509, 507 (bukan urutan nomor). TC-FA-CF-507 berjalan terakhir karena ganti akun ke `Rina Putri` dan mengubah nama pengguna (state global), sedangkan TC lain memakai akun `Sarah Johnson` yang login di hook `before`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 28 (ganti akun eksplisit), langkah 36 (mencatat Date dan jumlah baris hasil Search untuk perbandingan), baseline di awal TC-FA-CF-508, 509, dan 507 (TC-FA-CF-506 tidak memakai baseline jumlah; baseline TC-FA-CF-508 berupa jumlah baris hasil Search `Asset Serial Tag` per surface dan baseline TC-FA-CF-509 berupa jumlah entri System Log `Rina Putri`; termasuk langkah 29, baseline jumlah baris hasil Search `Total Cost` sebelum Deactivate; S-12), "Tunggu aksi selesai" sebelum surface log dibuka (8b butir 8) pada TC-FA-CF-506, 509, dan 507 (langkah 3, 22, 32, dan 38; langkah 38 sesudah ubah nama pengguna, asersi tambahan di luar Expected TC, S-03), dan langkah buka serta temukan baris di tiap surface (R-16).
- TC-FA-CF-507 (langkah 29 sampai 41): entri Deactivate `Total Cost` tidak unik pada audit trail permanen; "entri baru" dibuktikan dengan selisih satu baris hasil Search `Total Cost` terhadap baseline (langkah 34), dan "tidak ditulis ulang" dengan jumlah baris hasil Search yang sama dengan sebelum rename pengguna (langkah 41), bukan dengan "hanya ada satu entri" (S-12).
- TC-FA-CF-509 "pengguna lain" ditulis `Rina Putri` (Pre-setup #10) karena TC tidak menyebut pengguna lain tertentu; asersi isolasi log per aktor bukan kelas g (bagian 3 prinsip 13g) dan memakai anchor tab System Log `Rina Putri` tampil dengan jumlah entri sama dengan baseline.
- Temuan untuk QA:
  - TC-FA-CF-507 langkah 4 tidak menyebut aktor yang mengganti nama pengguna dan tidak menyatakan apakah `Rina Putri` memiliki izin Global Settings > User; spec memakai sesi `Rina Putri` yang sedang login.
  - TC-FA-CF-506 dan TC-FA-CF-508 tidak menyebut aktor selain "Total Control"; spec memakai `Sarah Johnson` (Pre-setup #1), sedangkan indeks TC memetakan spec ini ke Pre-setup #10 (Total Control sesi 2) karena TC-FA-CF-507.
  - TC-FA-CF-508 Expected "tanpa selisih" tidak mendefinisikan kolom yang dibandingkan; spec membandingkan Action, Field, Old Value, dan New Value.
  - Email akun Total Control Company Alpha sesi 2 mengikuti pola Pre-setup #10; env var `FA_TC2_PASSWORD` disediakan tim FE.
