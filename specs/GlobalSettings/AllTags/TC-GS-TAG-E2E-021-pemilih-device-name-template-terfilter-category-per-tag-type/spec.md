---
id: TC-GS-TAG-E2E-021-pemilih-device-name-template-terfilter-category-per-tag-type
title: "Pemilih Device Name Template Terfilter Category per TAG Type (GPS, RFID Object/User, NFC, BLE)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-354
coverage:
  web: automated
---

# Pemilih Device Name Template Terfilter Category per TAG Type (GPS, RFID Object/User, NFC, BLE)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Data: opsi mandiri (BYO) aktif; katalog Admin Console Client A (dibaca saja, tidak diubah; seeding dan akun Admin Console disediakan tim FE, S-13) memuat Device Name dengan Category: `Queclink GV300` dan `Teltonika FMB920` (`TAG > GPS`), `Zebra RFD40 Tag` (`TAG > RFID`), `Access Card Reader` (`TAG > NFC`), `Tag Reel` (`TAG > NFC > Tag`, turunan node `NFC`), `Asset Beacon Mini` (`TAG > BLE`), dan `Door Antenna` (`Hardware > Smart Fixed Reader > Antenna`, di luar konteks semua TAG Type).
- Tabel `TAG Type yang diuji` (urutan sesuai Data Uji TC-354; dipakai langkah 2 sampai 9):

  | TAG Type | Daftar opsi Device Name memuat | Daftar opsi Device Name tidak memuat |
  |---|---|---|
  | `GPS` | `Queclink GV300`, `Teltonika FMB920` | `Zebra RFD40 Tag`, `Access Card Reader`, `Tag Reel`, `Asset Beacon Mini`, `Door Antenna` |
  | `RFID – Object TAG` | `Zebra RFD40 Tag` | `Queclink GV300`, `Teltonika FMB920`, `Access Card Reader`, `Tag Reel`, `Asset Beacon Mini`, `Door Antenna` |
  | `RFID – User TAG` | `Zebra RFD40 Tag` | `Queclink GV300`, `Teltonika FMB920`, `Access Card Reader`, `Tag Reel`, `Asset Beacon Mini`, `Door Antenna` |
  | `NFC` | `Access Card Reader`, `Tag Reel` | `Queclink GV300`, `Teltonika FMB920`, `Zebra RFD40 Tag`, `Asset Beacon Mini`, `Door Antenna` |
  | `BLE` | `Asset Beacon Mini` | `Queclink GV300`, `Teltonika FMB920`, `Zebra RFD40 Tag`, `Access Card Reader`, `Tag Reel`, `Door Antenna` |

- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-354: Pemilih Device Name terfilter Category per TAG Type

1. Lakukan langkah 2 sampai 9 untuk setiap baris tabel `TAG Type yang diuji`
2. Mulai sesi Activate TAG tipe `<TAG Type>`: klik `+ Activate TAG`, pilih `<TAG Type>` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
3. Buka section `Self-Purchased Template`
4. Klik field Device Name dan amati daftar opsi
5. Verifikasi form aktivasi tidak memiliki field Category
6. Verifikasi field Device Name hanya memilih dari daftar katalog
7. Verifikasi daftar opsi Device Name memuat nilai pada kolom `Daftar opsi Device Name memuat` untuk `<TAG Type>`
8. Verifikasi daftar opsi Device Name tidak memuat nilai pada kolom `Daftar opsi Device Name tidak memuat` untuk `<TAG Type>`
9. Kembali ke List: klik item sidebar `TAG` (staging kosong)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (satu TC, dataset katalog read-only).
- Langkah 2 sampai 9 diulang untuk lima baris tabel (idiom "Untuk setiap baris tabel ... " butir 7 bagian 8b); ekspansi: 1 + 5 x 8 = 41 langkah, di atas sekitar 35. Alasan: satu TC, satu dataset (katalog Client A), satu kelas harness (fungsional), parameter tiap iterasi ada di tabel `TAG Type yang diuji` tanpa langkah bersyarat, dan tiap iterasi berdiri sendiri (sesi baru per TAG Type, karena tipe terkunci selama sesi).
- TC-354 Langkah 6 meminta mengulang langkah 1 sampai 5 untuk tiap TAG Type berikutnya "halaman Activate ditutup lebih dulu"; langkah 9 melakukannya dan `Verifikasi` yang diulang tetap satu per klausa Expected (a sampai f).
- Langkah penghubung (tanpa `Verifikasi`): langkah 2 menggabungkan TC langkah 1 sampai 3; membuka section Template dan klik field Device Name adalah TC langkah 4 dan 5; kolom `tidak memuat` menjalankan Expected b sampai f (termasuk `Door Antenna` tidak tampil pada TAG Type mana pun, Expected f).
- Rujukan: perilaku Template lain ada di spec 019 dan 020.
- Temuan untuk QA:
  - TC-354 Expected a menyebut "dibaca Client secara read-only" di Skenario tanpa langkah observasi; spec hanya mengasersi Client tidak memiliki field Category dan Device Name dipilih dari daftar katalog.
  - TC-354 Expected c menulis daftar RFID – Object TAG dan RFID – User TAG "sama"; spec mengasersi tiap tipe sendiri.
