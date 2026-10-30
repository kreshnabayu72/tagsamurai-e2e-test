---
id: TC-GS-HHR-E2E-015-activate-gate-kuota-habis-dan-kuota-terlampaui
title: "Gate Kuota Activate Reader: Insufficient License Quota saat Kuota Habis dan Kuota Terlampaui akibat Downgrade"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-54
  - TC-GS-HHR-55
  - TC-GS-HHR-56
coverage:
  web: automated
---

# Gate Kuota Activate Reader: Insufficient License Quota saat Kuota Habis dan Kuota Terlampaui akibat Downgrade

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah Alias Name satu reader Pre-setup Client O dan berganti akun antar Client.
- Akun aktor (disediakan tim FE; pola email `totalControl_automated_{namaClient}@qwertysystem.net` dari Tabel Pre-setup TC, nilai `{namaClient}` per client dari fixture baru `fixtures/hardwareHandheldReader.json`):

  | Blok | Client | Kondisi | Akun | Env var password |
  |---|---|---|---|---|
  | TC-GS-HHR-54, TC-GS-HHR-55 | Client Q | `Short Range` 2 dari 2 dan `Long Range` 3 dari 3 terpakai (0 remaining) | Total Control Client Q | `Spectra.env.GS_CLIENTQ_TC_PASSWORD` |
  | TC-GS-HHR-56 | Client O | `Short Range` diturunkan menjadi 2 dengan 3 reader Short Range terdaftar | Total Control Client O | `Spectra.env.GS_CLIENTO_TC_PASSWORD` |

  Nama env var baru ini belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Login Client Q di hook `before`; ganti akun ke Client O dilakukan di langkah 15 dan 16; hook `after` mengembalikan sesi ke akun default suite (Total Control Sari Dewi Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Layar awal Global Settings > Hardware > Handheld Reader dibuka hook `beforeEach` untuk akun hook `before`; sesudah ganti akun, langkah 17 membukanya.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`), termasuk akun Client Q dan Client O.
- Data Pre-setup: kondisi Client Q dan Client O di atas dipulihkan oleh fixture backend sebelum spec. Nama tiga reader Short Range Client O dan Alias Name awal reader target dibaca dari fixture baru (tidak tertulis di TC; lihat Temuan untuk QA). Data Dinamis: Alias Name `Reader Dock 01 {runId}-015`.
- Efek pada Pre-setup bersama: langkah 28 mengubah Alias Name satu reader Pre-setup Client O (Last Updated dan entri Changelog reader itu berubah). Hook `after` memulihkan Alias Name reader itu ke nilai awal dan state Client O ke Tabel Pre-setup TC (mekanisme fixture backend disediakan tim FE/BE).
- Kemampuan teknis: pembacaan kartu kuota `Short Range` dan `Long Range`; tidak memerlukan simulator USB (popup Activate tidak dibuka).
- Cleanup (hook `after`): tutup dialog atau popup yang masih terbuka, pulihkan Alias Name reader Client O, kembalikan sesi ke akun default.

## Test Steps

### TC-GS-HHR-54: Memilih Short Range saat kuota habis (Client Q)

1. Klik `[+ Activate Reader]`
2. Klik `Short Range` pada Overlay `Select Range Type`
3. Verifikasi Overlay `Select Range Type` tertutup
4. Verifikasi dialog `Insufficient License Quota` tampil dengan body `License quota reached for selected range type.` dan satu tombol `[OK]`
5. Verifikasi Popup `Activate Handheld Reader` tidak terbuka
6. Klik `[OK]`
7. Verifikasi dialog `Insufficient License Quota` tertutup
8. Verifikasi halaman kembali ke daftar reader

### TC-GS-HHR-55: Memilih Long Range saat kuota habis (Client Q)

9. Klik `[+ Activate Reader]`
10. Klik `Long Range` pada Overlay `Select Range Type`
11. Verifikasi dialog `Insufficient License Quota` tampil dengan body `License quota reached for selected range type.` dan tombol `[OK]`
12. Verifikasi Popup `Activate Handheld Reader` tidak terbuka
13. Klik `[OK]`
14. Verifikasi halaman kembali ke daftar reader

### Ganti akun ke Client O

15. Logout dari akun Total Control Client Q
16. Login sebagai Total Control Client O (`Spectra.env.GS_CLIENTO_TC_PASSWORD`)
17. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-56: Kuota terlampaui akibat downgrade (Client O)

18. Klik `[+ Activate Reader]`
19. Klik `Short Range` pada Overlay `Select Range Type`
20. Verifikasi dialog `Insufficient License Quota` tampil dengan body `License quota reached for selected range type.`
21. Verifikasi Popup `Activate Handheld Reader` tidak terbuka
22. Klik `[OK]`
23. Verifikasi tiga reader Short Range Client O (nama dari fixture) tetap tampil di tabel
24. Ketik Search dengan Device Name reader Short Range pertama Client O (dari fixture), tekan Enter
25. Klik `⋯` pada baris reader tersebut
26. Pilih `Edit Alias Name`
27. Isi `Alias Name` dengan `Reader Dock 01 {runId}-015`
28. Klik `[Save]`
29. Verifikasi `Alias Name` baris tersebut menjadi `Reader Dock 01 {runId}-015`
30. Klik `(←)` pada kotak Search
31. Verifikasi kartu `Short Range` menampilkan `3 of 2`
32. Verifikasi kartu `Short Range` menampilkan `0 remaining`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: blokir karena kondisi data (prinsip 12): kuota habis (Client Q) dan kuota terlampaui (Client O); dua client dalam satu spec dengan Step ganti akun eksplisit (langkah 15 sampai 17), bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`): langkah 15 sampai 17 (ganti akun dan buka halaman); langkah 24 (Search untuk menemukan baris target) dan langkah 30 (mengosongkan Search) menjadi penghubung sebelum dan sesudah Edit Alias Name.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-56 ditulis bersuffix per run (`Reader Dock 01 {runId}-015`) mengikuti S-12; asersi memakai nilai bersuffix yang sama.
- Langkah 23 menyebut "tiga reader Short Range" sesuai TC; nama ketiganya dari fixture. Langkah 8 dan 14 ("halaman kembali ke daftar reader") diasersi sebagai tampilnya tabel daftar reader setelah dialog tertutup.
- Tidak ada pencatatan log yang diasersi.
- Temuan untuk QA:
  - TC-GS-HHR-56 tidak menyebut nama tiga reader Short Range Client O, reader mana yang diedit pada langkah 4, atau Alias Name awalnya; spec memakai nama dari fixture baru (disediakan tim FE).
  - TC-GS-HHR-56 mengedit reader Pre-setup Client O karena kondisi kuota terlampaui hanya ada di Client O (data seed milik spec tidak mungkin, S-06); pemulihan Alias Name dan efeknya pada Last Updated dan Changelog dicatat di Prerequisites.
  - Email akun Client Q dan Client O mengikuti pola `{namaClient}` yang nilainya tidak tertulis di Tabel Pre-setup TC; password tiap client dibaca dari env var baru yang belum terdaftar.
  - TC-GS-HHR-56 Expected c hanya menyebut Alias Name berubah; toast sukses Edit Alias Name tidak diasersi karena tidak ada di Expected TC ini.
