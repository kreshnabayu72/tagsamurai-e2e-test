---
id: TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel
title: "Bulk Delete Homogen: Dialog, Confirm, Cancel, dan Satu Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-131
  - TC-GS-DIV-132
  - TC-GS-DIV-133
  - TC-GS-DIV-137
coverage:
  web: automated
---

# Bulk Delete Homogen: Dialog, Confirm, Cancel, dan Satu Baris

## Prerequisites

- Mode: FE+BE. Spec menghapus data (aksi destruktif) sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (kemampuan seeding Division lewat API di hook `before`; tidak menumpang spec lain), semuanya bebas relasi: `Marketing {runId}-037` dan `Logistics {runId}-037` (setara MKT dan LOG, dihapus pada TC-132 dan dipakai TC-131), `Engineering {runId}-037` dan `General Affairs {runId}-037` (TC-133), serta `Risk Management {runId}-037` (TC-137). Dependensi TC-GS-DIV-30 dipenuhi lewat seeding ini. Code hasil seeding mengikuti auto-generate dan tidak diasersi. Nama bersuffix per run dipakai karena asersi tidak bergantung pada nama literal; urutan bullet `Logistics` sebelum `Marketing` tetap terjaga.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API semua Division di atas yang masih ada, hapus isi kotak Search (`(←)`), dan bersihkan seleksi tabel. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Ketik Search `{runId}-037`, tekan Enter

### TC-GS-DIV-131: Bulk Delete seluruhnya bebas relasi memakai dialog homogen

2. Centang baris `Marketing {runId}-037`
3. Centang baris `Logistics {runId}-037`
4. Klik `Bulk Action` > `Delete`
5. Verifikasi Title dialog `Delete Division` (severity danger)
6. Verifikasi Body memuat bullet `Logistics {runId}-037` dan `Marketing {runId}-037`
7. Verifikasi Body memuat teks `Are you sure you want to delete them? This action cannot be undone.`
8. Verifikasi tombol `[Cancel]`
9. Verifikasi tombol `[Delete]` (filled, danger)
10. Klik `[Cancel]`
11. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-133: Cancel pada dialog Bulk Delete homogen tidak menghapus apa pun

12. Centang baris `Engineering {runId}-037`
13. Centang baris `General Affairs {runId}-037`
14. Klik `Bulk Action` > `Delete`
15. Klik `[Cancel]`
16. Verifikasi tidak ada toast
17. Verifikasi dialog tertutup
18. Verifikasi baris `Engineering {runId}-037` dan `General Affairs {runId}-037` tetap ada di tabel
19. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-137: Bulk Delete dengan satu baris bebas relasi memakai dialog single

20. Centang baris `Risk Management {runId}-037`
21. Klik `Bulk Action` > `Delete`
22. Verifikasi dialog `Delete Division` (judul sama untuk single dan bulk, tidak pernah jamak)
23. Verifikasi Body memuat bullet `Risk Management {runId}-037`
24. Verifikasi Body memuat teks `Are you sure you want to delete it? This action cannot be undone.`
25. Verifikasi tombol `[Cancel]`
26. Verifikasi tombol `[Delete]`
27. Klik `[Cancel]`
28. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-132: Konfirmasi Bulk Delete homogen menghapus seluruh Division terpilih

29. Centang baris `Marketing {runId}-037`
30. Centang baris `Logistics {runId}-037`
31. Klik `Bulk Action` > `Delete`
32. Klik `[Delete]` pada dialog
33. Verifikasi dialog tertutup
34. Verifikasi toast sukses `Success, division has been deleted.`
35. Verifikasi baris `Engineering {runId}-037` tampil di tabel (pembanding)
36. Verifikasi baris `Marketing {runId}-037` dan `Logistics {runId}-037` hilang dari tabel
37. Verifikasi Bulk Action Bar tertutup
38. Verifikasi seleksi bersih (tidak ada baris tercentang)

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC. Urutan di spec berbeda dari urutan sourceTc: TC-132 (Confirm yang menghapus `Marketing` dan `Logistics`) ditaruh paling akhir sesudah TC-131, TC-133, dan TC-137 (prinsip 5), karena TC-131 memakai pasangan baris yang sama sebelum dihapus.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search supaya Division milik spec tampil), 10 dan 27 (klik `[Cancel]` untuk menutup dialog yang di TC sumber tidak ditutup), 11, 19, dan 28 (klik `(✕)` untuk memulai TC berikutnya dari seleksi bersih).
- Asersi tambahan: langkah 35 (baris `Engineering {runId}-037` tampil) adalah baris pembanding sebelum asersi baris hilang (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (38 langkah) karena memuat empat TC dialog Bulk Delete homogen pada layar dan dataset milik spec yang sama dengan satu kelas harness (aksi destruktif). Blok memakai satu Search (langkah 1) dan Division seeding sendiri; TC-132 memakai pasangan `Marketing` dan `Logistics` yang sama dengan TC-131 sehingga ditaruh paling akhir. Memisahkannya mengulang login, seeding, dan Search yang sama, dan tiga TC pertama tidak menghapus data.
- Satu penghapusan sungguhan hanya di blok terakhir (TC-132); sisa Division (`Engineering`, `General Affairs`, `Risk Management`) dihapus lewat API di hook `after`.
- Temuan untuk QA:
  - TC-131 dan TC-132 menulis bullet `Logistics` dan `Marketing` (urut A-Z) pada dialog; spec memakai urutan yang sama dengan nama bersuffix.
  - TC-131 dan TC-137 tidak menyebut penutupan dialog; spec menambah klik `[Cancel]` sebagai langkah penghubung.
  - TC-132 Post Condition ("Division Marketing dan Logistics terhapus") punya padanan di butir c. TC-131, TC-133, dan TC-137 tanpa Post Condition yang punya langkah observasi di TC.
