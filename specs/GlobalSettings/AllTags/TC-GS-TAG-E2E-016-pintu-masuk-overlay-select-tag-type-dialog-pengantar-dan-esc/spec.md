---
id: TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc
title: "Pintu Masuk Activate TAG: Overlay Select TAG Type, Esc, Dialog Ready to Activate, dan Tipe Terkunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-36
  - TC-GS-TAG-37
  - TC-GS-TAG-38
  - TC-GS-TAG-42
coverage:
  web: automated
---

# Pintu Masuk Activate TAG: Overlay Select TAG Type, Esc, Dialog Ready to Activate, dan Tipe Terkunci

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Data: registri Client A berisi Seed Registri A (DD-01..DD-30), plan Growth, kuota tersedia untuk seluruh tipe (kuota RFID–Object TAG 50, RFID–User TAG 20, NFC 30, BLE 30, GPS 30); dipakai sebagai precondition TC, tidak diasersi.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-36: Screening overlay Select TAG Type

1. Klik `+ Activate TAG`
2. Verifikasi popover ter-anchor ke tombol `+ Activate TAG`
3. Verifikasi pilihan radio berurutan: `RFID – Object TAG | RFID – User TAG | NFC | BLE | GPS`
4. Verifikasi tipe `QR` tidak ada di daftar pilihan

### TC-GS-TAG-37: Esc menutup overlay tanpa membuka sesi

5. Tekan `Esc`
6. Verifikasi overlay `Select TAG Type` tertutup
7. Verifikasi halaman tetap di List
8. Verifikasi tidak ada popup `Ready to Activate a TAG`
9. Verifikasi halaman Activate TAG tidak terbuka sehingga tidak ada tipe terkunci
10. Klik `+ Activate TAG` lagi
11. Verifikasi overlay `Select TAG Type` tampil kembali tanpa pilihan terpilih

### TC-GS-TAG-38: Popup pengantar sesi (Dialog 2) dan Cancel

12. Pilih `RFID – Object TAG`
13. Verifikasi popup berjudul `Ready to Activate a TAG`
14. Verifikasi body popup `This session is locked to RFID – Object TAG. Scan the TAGs you want to activate, then review and submit them.`
15. Verifikasi tombol `Cancel` dan `Continue` tampil
16. Klik `Cancel`
17. Verifikasi popup tertutup
18. Verifikasi halaman tetap di List
19. Verifikasi halaman Activate TAG tidak terbuka

### TC-GS-TAG-42: Tipe terkunci selama sesi

20. Mulai sesi Activate TAG tipe `RFID – Object TAG`: klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
21. Verifikasi header menampilkan tipe terkunci `RFID – Object TAG`
22. Verifikasi tidak ada dropdown atau tombol ganti tipe di header maupun di kontrol halaman
23. Kembali ke List: klik item sidebar `TAG` (staging kosong)
24. Klik `+ Activate TAG`
25. Verifikasi overlay `Select TAG Type` tampil kembali sehingga tipe lain hanya dapat dipilih dengan mulai ulang dari `+ Activate TAG`
26. Tekan `Esc`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional biasa.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`): langkah 20 menggabungkan TC-42 langkah 1 sampai 3 (membuka sesi baru); `Kembali ke List` tanpa dialog karena staging kosong; `Esc` di akhir spec menutup overlay yang sengaja dibuka agar hook `after` memulai dari List bersih.
- Urutan TC-37 (kasus `Esc`) sebelum TC-38 dan TC-42 mengikuti prinsip 3 bagian 3 konvensi: kasus yang menutup tanpa membuka sesi tidak membuat data.
- Temuan untuk QA:
  - TC-37 Expected a menyebut "tidak ada tipe terkunci" tanpa cara mengamatinya di List; spec mengasersi bahwa halaman Activate TAG tidak terbuka (langkah 9).
  - TC-42 Expected b ("Satu-satunya cara memilih tipe lain") adalah klaim negatif universal; spec mengasersi tidak adanya kontrol ganti tipe (langkah 22) dan bahwa mulai ulang dari `+ Activate TAG` menampilkan overlay lagi (langkah 25), tanpa membuktikan tidak ada jalur lain.
  - TC sumber tidak menyatakan apakah keluar dari halaman Activate dengan staging kosong memunculkan dialog; spec menganggap tidak (dirty didefinisikan di spec 036, TC-183 sampai TC-185).
