---
id: TC-FA-TAG-E2E-233-modal-changelog-screening-penutupan-tooltip-dan-read-only-bagian-1
title: "Modal Changelog Paired TAG: Screening, Penutupan, Tooltip Toolbar, dan Read-only (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-931
  - TC-FA-TAG-932
  - TC-FA-TAG-933
  - TC-FA-TAG-934
  - TC-FA-TAG-935
  - TC-FA-TAG-936
  - TC-FA-TAG-937
  - TC-FA-TAG-938
  - TC-FA-TAG-968
  - TC-FA-TAG-975
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Screening, Penutupan, Tooltip Toolbar, dan Read-only (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG dengan tanggal dan pelaku persis seperti tabel di bawah; tidak ada endpoint yang dikarang di spec ini. Changelog dalam scope akun Total Control hanya memuat E1 sampai E6 selama spec berjalan; fixture mengembalikan keadaan itu di hook `before` dan `after`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E1 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [NFC] NF-00090 | [RFID] RF-00420 | Sari W. |
| E2 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [QR] QR-00240 | — | Sari W. |
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |
| E4 | 26/10/26 09:14 | Replace | Excavator 20 Ton - 42 | TAG | [QR] QR-00230 | [RFID] RF-00412 | Budi S. |
| E5 | 25/10/26 16:40 | Replace | Forklift Manual - 61 | TAG | [QR] QR-00251 | — | Dedi K. |
| E6 | 25/10/26 08:00 | Report TAG | Excavator 20 Ton - 20 | Report Type | — | Damaged | Rina T. |

  Kunci fixture: `changelogE1E6`.
- State yang diubah: hanya state tampilan modal; konfigurasi kolom tidak diubah spec ini. Tidak ada perubahan data bisnis.

## Test Steps

### Screening Modal Changelog (TC-FA-TAG-931, TC-FA-TAG-932)

1. Klik tombol `Changelog` pada Table Tools
2. Verifikasi judul modal `Changelog: Paired TAG`
3. Verifikasi ikon close `[✕]` tampil di header
4. Verifikasi Table Tools `Search | Filter | Download` tampil di header
5. Verifikasi kolom body `Date (sortable) | Action (sortable) | Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`
6. Verifikasi urutan Date terbaru di atas
7. Verifikasi Old Value dan New Value berupa teks polos tanpa badge
8. Verifikasi `—` tampil bila entri tanpa pasangan
9. Verifikasi Modified By berformat `[First Name] [Last Initial]`
10. Verifikasi footer Pagination default 10
11. Buka selector page size pada footer
12. Verifikasi pilihan page size 10 / 25 / 50 / 100
13. Tutup selector page size dengan memilih `10`

### Menutup lewat ikon close (TC-FA-TAG-933)

14. Klik ikon `[✕]`
15. Verifikasi modal tertutup
16. Verifikasi tab Paired tampil
17. Klik tombol `Changelog` pada Table Tools

### Menutup lewat Esc (TC-FA-TAG-934)

18. Tekan Esc
19. Verifikasi modal tertutup
20. Klik tombol `Changelog` pada Table Tools

### Klik backdrop (TC-FA-TAG-935)

21. Klik area gelap di luar modal
22. Verifikasi modal tetap terbuka

### Tooltip ikon toolbar (TC-FA-TAG-936, TC-FA-TAG-937, TC-FA-TAG-938)

23. Arahkan pointer ke ikon Search di toolbar modal
24. Verifikasi tooltip `Search` tampil
25. Arahkan pointer ke ikon Filter di toolbar modal
26. Verifikasi tooltip `Filter` tampil
27. Arahkan pointer ke ikon Download di toolbar modal
28. Verifikasi tooltip `Download` tampil

### Modal hanya-baca (TC-FA-TAG-968)

29. Verifikasi tidak ada aksi Edit atau Delete pada setiap entri Changelog
30. Verifikasi kolom `⋯` hanya untuk Column Visibility

### Tidak tersedia pada tab To Be Returned (TC-FA-TAG-975)

31. Klik ikon `[✕]` untuk menutup modal
32. Klik Tab `To Be Returned`
33. Verifikasi Tab `To Be Returned` aktif dan ikon Search pada Table Tools tampil
34. Verifikasi tidak ada tombol `Changelog` pada tab To Be Returned

## Notes

- Langkah penghubung (S-03): langkah 11 sampai 13 (membuka dan menutup selector page size untuk mengamati pilihan TC-FA-TAG-931 Expected c), 17 dan 20 (membuka kembali modal sesudah ditutup), dan 31 (menutup modal sebelum pindah tab).
- TC-FA-TAG-932 (judul modal dari halaman TAG) memakai aksi yang sama dengan TC-FA-TAG-931 langkah 1; Expected-nya dicakup `Verifikasi` langkah 2.
- Langkah 29 mengamati setiap entri pada halaman yang tampil (enam entri E1 sampai E6 menurut Prerequisites).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-968 ("Konfigurasi kolom tersimpan di cache browser sesuai langkah yang dilakukan") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-FA-TAG-968 langkah 2 "Periksa setiap baris dan kolom Column Visibility" tidak menyebut aksi yang dilakukan; spec hanya mengamati baris dan header kolom `⋯`.
  - TC-FA-TAG-931 Expected b tidak menyebut format teks Date yang tampil; asersi urutan memakai tanggal Data Uji.
  - Post Condition TC lain ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi urutan dan isi bergantung pada keadaan Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
