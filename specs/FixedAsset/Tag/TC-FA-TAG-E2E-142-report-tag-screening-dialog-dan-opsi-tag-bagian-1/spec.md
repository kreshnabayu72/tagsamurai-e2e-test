---
id: TC-FA-TAG-E2E-142-report-tag-screening-dialog-dan-opsi-tag-bagian-1
title: "Report TAG: Screening Dialog dan Opsi Tag (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-598
  - TC-FA-TAG-599
  - TC-FA-TAG-600
  - TC-FA-TAG-601
  - TC-FA-TAG-602
  - TC-FA-TAG-603
coverage:
  web: automated
---

# Report TAG: Screening Dialog dan Opsi Tag (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |
| Aset 'Server Rack 42U - 201' | AST-0201, dua Tag RFID Paired `RF-00201` dan `RF-00202` tanpa laporan terbuka, item di task Existence Audit yang sama | `aset201` |

- State yang diubah dan pemulihannya: laporan terbuka pada `RF-00132` dan `RF-00130` (langkah 23) dibatalkan dan data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 23) yang menyiapkan atau memulihkan state.

## Test Steps

### Dialog Report TAG pada aset satu Tag (TC-FA-TAG-598)

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Verifikasi dialog "Report TAG" terbuka di atas halaman Task Detail
4. Verifikasi blok info aset menampilkan judul "Excavator 20 Ton - 20", Asset ID "AST-0020", ikon tipe Tag RFID, serta grid Brand, Model/Type, Group, dan Asset Status
5. Verifikasi bagian "TAG to report" bertanda wajib (*) menampilkan satu opsi berlabel "RFID" tanpa checkbox
6. Verifikasi opsi "RFID" otomatis terpilih
7. Verifikasi Radio "Report Type" bertanda wajib (*) tersusun mendatar dengan opsi "Damaged", "Missing", dan "Unreadable"
8. Verifikasi belum ada opsi Report Type yang terpilih
9. Verifikasi Textarea "Note" bertanda wajib (*) kosong
10. Verifikasi footer berisi tombol [Cancel] dan [Submit]
11. Verifikasi dialog tidak memuat checkbox `Stay on this form after submitting`
12. Klik [Cancel] pada dialog "Report TAG"

### Dialog Report TAG pada aset dua Tag (TC-FA-TAG-599)

13. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
14. Verifikasi bagian "TAG to report" menampilkan dua checkbox tersusun mendatar berlabel "RFID" dan "QR"
15. Verifikasi kedua checkbox belum tercentang
16. Verifikasi Radio "Report Type" kosong (belum ada opsi terpilih)
17. Verifikasi Textarea "Note" kosong
18. Klik [Cancel] pada dialog "Report TAG"

### Label opsi pada aset dengan dua Tag bertipe sama (TC-FA-TAG-602)

19. Pilih row action "Report TAG" pada baris Server Rack 42U - 201
20. Verifikasi dua checkbox tampil pada bagian "TAG to report"
21. Verifikasi label tiap opsi memuat tipe "RFID" beserta TAG Code ("RF-00201" dan "RF-00202") agar keduanya dapat dibedakan
22. Klik [Cancel] pada dialog "Report TAG"

### Opsi Tag dengan laporan terbuka (TC-FA-TAG-600 dan TC-FA-TAG-601)

23. Atur ulang data lewat fixture backend: Tag RF-00132 punya laporan terbuka Missing (Tag QR-00232 tanpa laporan terbuka) dan Tag RF-00130 punya laporan terbuka Damaged hingga tersimpan, lalu muat ulang halaman Task Detail
24. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
25. Arahkan kursor ke opsi "RFID" yang Disabled
26. Verifikasi opsi "RFID" tetap tampil dalam keadaan Disabled dan tidak dapat dicentang
27. Verifikasi tooltip "This TAG already has an open report." tampil
28. Verifikasi opsi "QR" tercentang awal karena hanya satu Tag yang dapat dilaporkan
29. Klik opsi "RFID" yang Disabled
30. Verifikasi opsi "RFID" tetap tidak tercentang
31. Verifikasi opsi "QR" tetap satu-satunya yang tercentang
32. Klik [Cancel] pada dialog "Report TAG"

### Aksi Report TAG Hidden bila semua Tag sudah berlaporan (TC-FA-TAG-603)

33. Buka menu aksi baris Excavator 20 Ton - 20
34. Verifikasi aksi "Report TAG" Hidden pada baris tersebut

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-598 s.d. 603). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-604 ada di spec 143.
- Urutan TC di dalam spec: TC-598, TC-599, TC-602, TC-600, TC-601, TC-603. TC-602 diletakkan sebelum TC-600 dan TC-601 karena ketiganya membutuhkan state laporan berbeda; langkah 23 membangun state TC-600, TC-601, dan TC-603 sekaligus (laporan terbuka pada `RF-00132` dan `RF-00130`) sehingga TC-603 tidak membutuhkan seeding tersendiri.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 23 (mengatur ulang data lewat fixture backend dan memuat ulang halaman) serta semua langkah `Klik [Cancel] pada dialog "Report TAG"` yang menutup dialog sebelum TC berikutnya.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 23) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - TC tidak menyatakan apakah satu-satunya Tag yang terpilih otomatis membuat dialog dianggap terisi saat ditutup; spec menutup dialog yang belum diisi pengguna dengan [Cancel] atau [Keep Report] tanpa dialog Unsaved Changes, mengikuti TC-FA-TAG-666 dan TC-FA-TAG-675.
  - TC-FA-TAG-598 menulis "dipilih otomatis" untuk satu Tag tanpa checkbox, tetapi TC-FA-TAG-600 menulis opsi "QR" "tercentang awal"; spec mengikuti masing-masing TC (opsi tanpa checkbox terpilih otomatis pada TC-598, checkbox tercentang pada TC-600).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
