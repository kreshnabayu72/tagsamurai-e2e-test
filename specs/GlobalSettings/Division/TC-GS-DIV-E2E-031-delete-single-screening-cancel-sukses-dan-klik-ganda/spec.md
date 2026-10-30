---
id: TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda
title: "Delete Division Single: Screening Dialog, Cancel, Sukses, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-114
  - TC-GS-DIV-115
  - TC-GS-DIV-116
  - TC-GS-DIV-124
coverage:
  web: automated
---

# Delete Division Single: Screening Dialog, Cancel, Sukses, dan Klik Ganda

## Prerequisites

- Mode: FE+BE. Spec menghapus data (aksi destruktif) sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (kemampuan seeding Division lewat API di hook `before`; tidak menumpang spec lain), semuanya bebas relasi: `Public Relations {runId}-031` (setara D-10, dependensi TC-GS-DIV-65 untuk TC-114, TC-115, dan TC-116; dihapus spec ini), `Facilities {runId}-031` (dependensi TC-GS-DIV-30 untuk TC-124; dihapus spec ini), dan `Anchor Unit {runId}-031` (baris pembanding yang tetap ada untuk asersi baris hilang pada TC-116 dan TC-124; tidak dihapus oleh langkah spec). Code hasil seeding mengikuti auto-generate dan tidak diasersi. Nama bersuffix per run dipakai karena asersi tidak bergantung pada nama literal.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga Division di atas bila masih ada. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: menahan respons Delete lewat intercept untuk mengamati state `[Delete]` disabled setelah klik pertama (TC-124), lalu melepaskannya; klik ganda cepat pada tombol dialog; membuka Modal Changelog Division dari toolbar tabel.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Ketik Search `{runId}-031`, tekan Enter

### TC-GS-DIV-114: Screening dialog konfirmasi Delete single

2. Buka row action baris `Public Relations {runId}-031` lalu klik `Delete`
3. Verifikasi Title dialog `Delete Division` (severity danger)
4. Verifikasi Body memuat bullet `Public Relations {runId}-031`
5. Verifikasi Body memuat teks `Are you sure you want to delete it? This action cannot be undone.`
6. Verifikasi tombol `[Cancel]` (text, contrast)
7. Verifikasi tombol `[Delete]` (filled, danger)

### TC-GS-DIV-115: Cancel pada dialog Delete tidak menghapus Division

8. Klik `[Cancel]`
9. Verifikasi tidak ada toast
10. Verifikasi dialog tertutup
11. Verifikasi baris `Public Relations {runId}-031` tetap ada di tabel

### TC-GS-DIV-116: Delete Division bebas relasi berhasil

12. Buka row action baris `Public Relations {runId}-031` lalu klik `Delete`
13. Klik `[Delete]` pada dialog
14. Verifikasi dialog tertutup
15. Verifikasi toast sukses `Success, division has been deleted.`
16. Verifikasi baris `Anchor Unit {runId}-031` tampil di tabel (pembanding)
17. Verifikasi baris `Public Relations {runId}-031` hilang dari tabel

### TC-GS-DIV-124: Klik ganda Delete hanya memproses satu penghapusan

18. Buka row action baris `Facilities {runId}-031` lalu klik `Delete`
19. Tahan respons Delete lewat intercept
20. Klik `[Delete]` dua kali cepat
21. Verifikasi tombol `[Delete]` disabled setelah klik pertama
22. Lepaskan respons Delete yang ditahan
23. Verifikasi hanya 1 toast sukses `Success, division has been deleted.`
24. Verifikasi baris `Anchor Unit {runId}-031` tampil di tabel (pembanding)
25. Verifikasi baris `Facilities {runId}-031` hilang dari tabel
26. Buka Modal Changelog Division dari toolbar tabel
27. Ketik Search `Facilities {runId}-031` pada Modal Changelog, tekan Enter
28. Verifikasi Changelog memuat tepat 1 entri `Delete` untuk `Facilities {runId}-031`
29. Tutup Modal Changelog lewat `✕`
30. Kosongkan isi kotak search lewat `(✕)`, tekan Enter

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC. TC-114 dan TC-115 berbagi satu pembukaan dialog (TC-115 melanjutkan dari dialog yang sama; langkah "Buka row action ... lalu klik `Delete`" TC-115 sumber digabung ke langkah 2). TC-116 membuka dialog lagi karena dialog sudah ditutup oleh `[Cancel]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (pencarian `{runId}-031` supaya seluruh Division milik spec tampil; Search tabel tidak diganti sampai langkah 30), 19 dan 22 (menahan dan melepas respons Delete supaya state disabled teramati sebelum respons selesai), 26 dan 27 (membuka Modal Changelog dan mencari Division), 29 dan 30 (menutup Modal Changelog dan membersihkan Search tabel).
- Asersi tambahan: langkah 16 dan 24 (baris `Anchor Unit` tampil) adalah baris pembanding sebelum asersi baris hilang (bagian 8b butir 2).
- Urutan TC di spec: TC-114, TC-115, TC-116, lalu TC-124. Aksi yang menghapus data (TC-116 dan TC-124) ditaruh sesudah screening dan Cancel (prinsip 5).
- Asersi "1 entri log Delete" TC-124 butir b ditulis sebagai asersi jumlah ("tepat 1 entri `Delete` untuk Division") di Modal Changelog, bukan asersi absence kelas g. Hitungan tepat 1 sudah menyatakan tidak ada entri Delete kedua. Nama Division bersuffix unik per run, sehingga tidak butuh baseline.
- Division memakai nama bersuffix `{runId}-031` (bukan nama literal Population D-02 `Facilities` atau D-10 `Public Relations`) karena spec menghapusnya dan asersi tidak bergantung pada nama literal.
- Temuan untuk QA:
  - TC-114 sampai TC-116 mensyaratkan dependensi TC-GS-DIV-65 (Create Public Relations) dan TC-124 mensyaratkan TC-GS-DIV-30; spec menyiapkannya lewat seeding API sendiri. TC tidak menyebut cara seeding.
  - TC-124 butir a ("`[Delete]` disabled setelah klik pertama") hanya teramati bila respons Delete ditahan; TC tidak menyebut cara mengamatinya. Spec memakai intercept penahan respons.
  - TC-124 butir b ("1 entri log Delete") tidak menyebut surface log; spec memakai Modal Changelog Division. Pencatatan di System Log aktor dan Activity Log dicakup spec pencatatan log.
  - TC-116 dan TC-124 Post Condition ("Division terhapus") punya padanan di Expected (baris hilang dari tabel). TC-115 Post Condition ("Division Public Relations tidak berubah") punya padanan di butir b.
