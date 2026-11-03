---
id: TC-AC-SG-E2E-015-mobile-android-long-press-selection-mode-dan-bulk-delete
title: "Mobile Android: Long-Press Masuk Selection Mode dan Bulk Delete Tersedia"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-393
coverage:
  web: unsupported
  mobile: automated
---

# Mobile Android: Long-Press Masuk Selection Mode dan Bulk Delete Tersedia

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android TAG Samurai (PRD §4.6).
- Perangkat atau emulator Android dengan aplikasi terpasang (Pre-setup #37), serta kemampuan tap, long-press (~500ms), ketik, dan mengetuk elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Pre-setup #37 menyebut "akun Total Control Principal uji" tanpa email; spec memakai akun Pre-setup #1 (lihat Temuan untuk QA). Login di aplikasi Android dilakukan di hook `before` spec ini.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini. Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` untuk akun aktor disetel `seen` oleh hook suite (kemampuan disediakan tim FE/BE; lihat `suite.md`).
- Data Dinamis (dibuat spec lewat Fixture BE di hook `before`, level 1 pada entitas Principal, tanpa entitas dan tanpa member; dipakai sebagai precondition TC "minimal dua card group tanpa member", dihapus oleh Bulk Delete pada langkah 19 dan oleh hook `after` bila spec berhenti di tengah):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-AC-SG-393 | dua card group tanpa member | `Mobile Hapus 1 {runId}-015` | Group level 1, tanpa entitas |
| TC-AC-SG-393 | dua card group tanpa member | `Mobile Hapus 2 {runId}-015` | Group level 1, tanpa entitas |

- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak tertulis di TC, PRD, atau LLD): Fixture BE untuk membuat dan menghapus group seed di atas; deteksi haptic ringan pada perangkat saat long-press (Expected a).
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group). Group seed menambah dua group selama spec berjalan; efek pada Last Updated dan Modified By node lain tidak ada karena group seed level 1.

## Test Steps

### TC-AC-SG-393: Mobile: long-press masuk selection mode dan Bulk Delete tersedia

1. Buka menu `Settings > Group` di aplikasi mobile
2. Ketuk ikon pencarian `[🔍]`, ketik "Mobile Hapus", lalu submit
3. Verifikasi card `Mobile Hapus 1 {runId}-015` dan `Mobile Hapus 2 {runId}-015` tampil di Card List
4. Long-press (~500ms) pada card `Mobile Hapus 1 {runId}-015`
5. Verifikasi selection mode aktif
6. Verifikasi haptic ringan terdeteksi saat selection mode aktif
7. Verifikasi card yang ditekan terpilih
8. Verifikasi checkbox muncul di semua card
9. Verifikasi Floating Bottom Bulk Action Bar tampil dengan penghitung "1 Selected"
10. Ketuk card `Mobile Hapus 2 {runId}-015`
11. Verifikasi ketukan pada card lain men-toggle checkbox card itu, bukan membuka aksi lain
12. Ketuk `[✕]` untuk keluar dari selection mode
13. Verifikasi seleksi dibatalkan
14. Verifikasi seluruh checkbox disembunyikan kembali
15. Long-press (~500ms) pada card `Mobile Hapus 1 {runId}-015`
16. Ketuk card `Mobile Hapus 2 {runId}-015`
17. Pada bilah aksi massal bawah, ketuk `Delete`
18. Verifikasi dialog Bulk Delete sama dengan web: Title "Delete Groups", bullet `Mobile Hapus 1 {runId}-015` dan `Mobile Hapus 2 {runId}-015` serta "Are you sure you want to delete them? This action cannot be undone." dengan tombol `[Cancel]` dan `[Delete]`
19. Ketuk `[Delete]` pada dialog
20. Verifikasi toast sukses "Success, group has been deleted."
21. Verifikasi card `Mobile Hapus 1 {runId}-015` dan `Mobile Hapus 2 {runId}-015` hilang dari Card List
22. Ketuk `✕` pada kotak Search untuk mengosongkan pencarian

## Notes

- Urutan langkah TC mengikuti state (S-10, bagian 8b butir 5): langkah TC 4 (`[✕]` pada percobaan terpisah) dijalankan lebih dulu (langkah 12) dan Bulk Delete yang menghapus data ditaruh di akhir (langkah 15 sampai 21), dengan seleksi diulang pada langkah 15 dan 16.
- Langkah penghubung (S-03, R-16): langkah 2 (Search untuk menemukan card seed), langkah 15 dan 16 (membangun ulang seleksi sesudah `[✕]`), langkah 22 (mengosongkan Search). Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web.
- Dialog dan toast Bulk Delete (langkah 18 dan 20) memakai teks dialog bulk homogen dan toast web dari TC-AC-SG-157, karena Expected c TC hanya menyebut "sama dengan web (PRD §7)". Absence langkah 21 berjangkar pada toast sukses yang sudah diasersi (langkah 20).
- Temuan untuk QA:
  - TC-AC-SG-393 Expected c ("memakai guard, dialog, dan toast hasil yang sama dengan web") tidak menyebut teks dialog dan toast, dan data uji (dua group tanpa member) hanya mengaktifkan jalur homogen D-06; guard member, would-empty, dan cascade tidak teruji di TC ini.
  - TC-AC-SG-393 Expected a ("haptic ringan") membutuhkan deteksi haptic di perangkat; mekanismenya tidak dijelaskan, ditulis sebagai kemampuan "disediakan tim FE/BE" (S-13).
  - Pre-setup #37 tidak menyebut email akun Total Control Principal untuk mobile; spec memakai akun Pre-setup #1. TC bertanda `Manual Only`; spec tetap ditulis dengan perangkat Android yang dibutuhkan dicatat di Prerequisites.
  - TC-AC-SG-393 precondition "minimal dua card group tanpa member" tidak menunjuk Pre-setup bernomor; spec men-seed dua group milik spec (S-06).
