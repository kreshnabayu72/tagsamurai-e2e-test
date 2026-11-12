---
id: TC-FA-GRP-E2E-089-android-delete-single-dan-bulk-delete-long-press-floating-bottom-bulk-bar
title: "Android: Seleksi Massal Hanya Long-Press dengan Floating Bottom Bulk Bar dan Delete Single/Bulk Memakai Dialog dan Toast Sama dengan Desktop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-983
  - TC-FA-GRP-984
coverage:
  mobile: automated
---

# Android: Seleksi Massal Hanya Long-Press dengan Floating Bottom Bulk Bar dan Delete Single/Bulk Memakai Dialog dan Toast Sama dengan Desktop

## Prerequisites

- Mode: FE+BE (mobile). Platform: aplikasi native Android TAG Samurai Mobile, halaman Groups. Perangkat atau emulator Android dengan aplikasi terpasang, kemampuan mengetuk, menekan lama, dan membaca elemen UI disediakan tim FE. Perangkat fisik bersama: `parallel: false` (S-09). Spec ini tidak memakai hook web suite.
- Login di hook `before` spec ini sebagai Total Control di aplikasi Android (Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`); halaman Groups dibuka hook `beforeEach`. Hook `after` mengembalikan sesi ke akun default suite.
- Nama data Dinamis ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-089`, sama di seeding, asersi teks, dan cleanup. Fixture `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Mob Kid 1` (child `Head Office`), `Del Empty Android`, `Bulk E14`, `Bulk E15`, `Bulk E16`. Data Pre-setup (Tabel A, No 9; hanya dibaca): `Head Office`, `Floor 2` (child `Head Office`), `Warehouse A` (beraset; di-skip oleh Delete campuran).
- Selektor: layar mobile belum punya ID atau aria-label di sumber; diselesaikan tim FE di tahap script.
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### TC-FA-GRP-983: Seleksi massal hanya lewat long-press card

1. Pilih `Head Office`, lalu tap satu card (`Floor 2`)
2. Verifikasi tap biasa tidak masuk selection mode (tidak ada Floating Bottom Bulk Bar)
3. Verifikasi tidak ada jalur seleksi massal selain long-press (daftar card tampil tanpa checkbox atau tombol pilih)
4. Long-press card `Floor 2`
5. Verifikasi selection mode aktif dan Floating Bottom Bulk Bar tampil
6. Verifikasi Floating Bottom Bulk Bar memuat aksi `Delete` sebagai satu-satunya bulk action
7. Tap card `Mob Kid 1`
8. Verifikasi seleksi bertambah (dua card terpilih)
9. Tap aksi `Delete` pada Floating Bottom Bulk Bar
10. Verifikasi dialog "Delete Groups" (D-17) sama dengan desktop
11. Batalkan dialog, lalu keluar dari selection mode

### TC-FA-GRP-984: Delete single dan bulk memakai dialog dan toast sama dengan desktop

12. Buka row action `⋯` card `Del Empty Android`, pilih `Delete`
13. Verifikasi dialog "Delete Group" (D-16)
14. Tap [Delete]
15. Verifikasi toast sukses "Success, group has been deleted."
16. Long-press card `Bulk E14`, lalu tap card `Bulk E15`
17. Tap aksi `Delete` pada Floating Bottom Bulk Bar
18. Verifikasi dialog "Delete Groups" (D-17)
19. Tap [Delete]
20. Verifikasi toast sukses "Success, group has been deleted."
21. Long-press card `Bulk E16`, lalu tap card `Warehouse A`
22. Tap aksi `Delete` pada Floating Bottom Bulk Bar
23. Verifikasi dialog campuran "Delete Groups" (D-18)
24. Tap [Continue]
25. Verifikasi toast "Success, group has been deleted. Some items were skipped."

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 11: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah dialog dan toast pada TC-984 mengikuti dialog D-10 sampai D-22 (kecuali D-14, tidak dipakai) serta toast T-06 dan T-08 yang sama dengan desktop; teks dialog desktop diasersi pada spec Delete di atas, sedangkan di sini yang diasersi adalah judul dialog dan toast sesuai Expected.
- Temuan untuk QA:
  - TC-983 Langkah 1 tidak menyebut hasil tap biasa pada card selain "tidak masuk selection mode"; spec hanya mengasersi tidak ada Floating Bottom Bulk Bar dan tidak ada kontrol seleksi massal.
  - TC-983 Precondition menyebut `Floor 2` kosong, sedangkan `Floor 2` Pre-setup memiliki child beraset; dialog hanya dibuka lalu dibatalkan sehingga tidak ada yang dihapus.
  - TC-984 mencampur kode dialog (D-16, D-17, D-18) dengan teks dialog; spec mengasersi judul dialog dan toast dari Expected.
