---
id: TC-GS-DIV-E2E-038-bulk-delete-campuran-dialog-continue-dan-cancel
title: "Bulk Delete Campuran: Dialog Dua Kelompok, Continue, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-134
  - TC-GS-DIV-135
  - TC-GS-DIV-287
coverage:
  web: automated
---

# Bulk Delete Campuran: Dialog Dua Kelompok, Continue, dan Cancel

## Prerequisites

- Mode: FE+BE. Spec menghapus data (aksi destruktif) sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah atau dihapus spec ini): `Human Resources` (HR, in-use Login User aktif Budi Santoso; nama literal tanpa suffix karena tidak dibuat atau diubah). Bulk Delete memperlakukan `Human Resources` sebagai item yang dilewati (no-op): data dan Last Updated tidak berubah.
- Data dinamis (kemampuan seeding Division lewat API di hook `before`; tidak menumpang spec lain), keduanya bebas relasi: `Data Analytics {runId}-038` (setara DA, dihapus pada TC-135) dan `Engineering {runId}-038` (setara ENG, tidak dihapus pada TC-287). Dependensi TC-GS-DIV-30 dipenuhi lewat seeding ini. Code hasil seeding mengikuti auto-generate dan tidak diasersi.
- Opsi page size 50 tersedia pada paginasi tabel, supaya `Human Resources` dan Division milik spec berada pada halaman yang sama.
- Kemampuan teknis: membuka Modal Changelog Division dari toolbar tabel dan membaca jumlah total entri yang tampil (TC tidak menyebut cara membaca jumlah; disediakan tim FE).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API `Data Analytics {runId}-038` dan `Engineering {runId}-038` bila masih ada, pulihkan page size (10), dan bersihkan seleksi tabel. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan dan baseline log

1. Ubah page size tabel menjadi 50
2. Buka Modal Changelog Division dari toolbar tabel
3. Catat jumlah total entri Changelog sebagai baseline (penanda sebelum aksi pada langkah 5 sampai 8)
4. Tutup Modal Changelog lewat `✕`

### TC-GS-DIV-287: Cancel pada dialog Bulk Delete campuran tidak menghapus apa pun

5. Centang baris `Human Resources`
6. Centang baris `Engineering {runId}-038`
7. Klik `Bulk Action` > `Delete`
8. Klik `[Cancel]` pada dialog `Delete Division`
9. Verifikasi tidak ada toast
10. Verifikasi dialog `Delete Division` tertutup
11. Verifikasi baris `Human Resources` dan `Engineering {runId}-038` tetap ada di tabel
12. Buka Modal Changelog Division dari toolbar tabel
13. Verifikasi jumlah total entri Changelog sama dengan baseline langkah 3 (tidak ada entri log baru)
14. Tutup Modal Changelog lewat `✕`
15. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-134: Bulk Delete campuran menampilkan Dialog campuran dengan dua kelompok

16. Centang baris `Human Resources`
17. Centang baris `Data Analytics {runId}-038`
18. Klik `Bulk Action` > `Delete`
19. Verifikasi Title dialog `Delete Division` (severity warning)
20. Verifikasi Body memuat `The following will be deleted:` dengan bullet `Data Analytics {runId}-038`
21. Verifikasi Body memuat `The following are still in use and will be skipped:` dengan bullet `Human Resources`
22. Verifikasi Body memuat `Are you sure you want to continue? This action cannot be undone.`
23. Verifikasi tombol `[Cancel]`
24. Verifikasi tombol `[Continue]` (filled, danger)

### TC-GS-DIV-135: Continue pada Bulk Delete campuran menghapus yang aman dan melewati yang in-use

25. Klik `[Continue]`
26. Verifikasi toast sukses `Success, division has been deleted. Some items were skipped.`
27. Verifikasi Division `Human Resources` tetap ada di tabel
28. Verifikasi Division `Data Analytics {runId}-038` terhapus: baris hilang dari tabel
29. Buka Modal Changelog Division dari toolbar tabel
30. Verifikasi jumlah total entri Changelog bertambah tepat 1 dari baseline langkah 3
31. Verifikasi entri baru tersebut adalah `Delete` untuk `Data Analytics {runId}-038`
32. Tutup Modal Changelog lewat `✕`
33. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC. Urutan di spec berbeda dari urutan sourceTc: TC-287 (Cancel) ditaruh pertama karena tidak menghapus data, lalu TC-134 dan TC-135 digabung dalam satu pembukaan dialog (langkah 16 sampai 18 adalah langkah 1 dan 2 TC-134 sekaligus TC-135; langkah "Klik `[Continue]`" TC-135 adalah langkah 25), dan aksi yang menghapus data (`[Continue]`) paling akhir (prinsip 5).
- Butir Expected TC-135 diurutkan menurut state: toast (butir b, langkah 26) diasersi tepat sesudah `[Continue]`, baru baris tabel (butir a, langkah 27 dan 28), karena toast adalah state sementara (bagian 8b butir 5); `Human Resources` tetap ada (langkah 27) sekaligus baris pembanding sebelum asersi `Data Analytics` hilang (bagian 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (page size 50 supaya `Human Resources` dan Division milik spec berada pada satu halaman), 2 sampai 4 (baseline jumlah entri Changelog sebelum aksi, S-12), 12 dan 14, 29 dan 32 (membuka dan menutup Modal Changelog), 15 (klik `(✕)` untuk memulai TC berikutnya dari seleksi bersih), 33 (memulihkan page size).
- Asersi log: TC-287 butir c ("Tidak ada entri log baru") ditulis di spec ini sebagai asersi jumlah dengan baseline (langkah 13: jumlah total entri sama dengan baseline setelah aksi nyata Cancel pada langkah 8), karena TC-287 tidak masuk spec absence. TC-135 butir c ("Hanya 1 entri log Delete tercatat untuk `Data Analytics`") ditulis sebagai kenaikan tepat 1 entri terhadap baseline yang sama dan entri baru itu `Delete` untuk `Data Analytics {runId}-038` (langkah 30 dan 31); tidak ada entri Delete untuk `Human Resources` karena jumlah hanya naik 1. Keputusan penempatan asersi tidak ada entri TC-287: lihat Temuan untuk QA.
- Division Pre-setup `Human Resources` tidak diberi suffix `{runId}` dan tidak diubah; `Data Analytics` dan `Engineering` memakai nama bersuffix karena spec menghapusnya atau menjadikannya objek uji dan asersi tidak bergantung pada nama literal.
- Temuan untuk QA:
  - TC-287 butir c ("Tidak ada entri log baru") adalah asersi absence, tetapi TC-287 tidak ada di `sourceTc` spec absence (067). Spec ini mengasersinya sebagai selisih jumlah entri Changelog terhadap baseline (aksi nyata Cancel ada dan baseline ada). Butir `P-1` yang disyaratkan S-05 tidak dipakai karena tidak ada state berat; perlu keputusan QA apakah TC-287 dimasukkan ke spec 067.
  - TC-135 butir c dan TC-287 butir c tidak menyebut surface log; spec memakai Modal Changelog Division. Cara membaca jumlah total entri tidak disebut TC dan disediakan tim FE.
  - TC-134 dan TC-135 memakai dialog yang sama dan menjadi satu pembukaan (lihat Notes).
  - TC-134, TC-135, dan TC-287 tidak menyebut cara menampilkan baris `Human Resources` dan Division lain pada halaman yang sama; spec memakai page size 50.
  - TC-134 dan TC-287 tanpa Post Condition yang punya langkah observasi tambahan; TC-135 Post Condition ("Data Analytics terhapus; Human Resources tetap") punya padanan di butir a.
