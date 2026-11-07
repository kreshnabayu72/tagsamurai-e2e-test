---
id: TC-FA-SU-E2E-072-validasi-submit-modal-assign-transaction-role-semua-kosong-sebagian-kosong-dan-clear
title: "Validasi Submit Modal Assign Transaction Role: Semua Kosong, Sebagian Kosong, dan Clear Field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-239
  - TC-FA-SU-240
  - TC-FA-SU-241
coverage:
  web: automated
---

# Validasi Submit Modal Assign Transaction Role: Semua Kosong, Sebagian Kosong, dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting).
- Data uji: Group Finance & Accounting, Transaction Disposal, Role Asset Admin (TC-FA-SU-240 dan 241). Semua `[Submit]` pada spec ini ditolak validasi atau dikosongkan sebelum dikirim; tidak ada penugasan yang disimpan.
- Kemampuan teknis (disediakan tim FE): pencatat request jaringan Spectra untuk memastikan tidak ada request simpan penugasan Transaction Role yang terkirim saat `[Submit]` (langkah 6).
- State global yang diubah: tidak ada; checkbox `Stay on this form after submitting` dikembalikan tidak tercentang pada langkah penghubung.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-239: Submit dengan semua field kosong: pesan wajib isi muncul inline di bawah tiap field

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu klik `[Submit]` tanpa mengisi apa pun
2. Verifikasi pesan "Group must not be empty" di bawah field Group
3. Verifikasi pesan "Transaction must not be empty" di bawah field Transaction
4. Verifikasi pesan "Role must not be empty" di bawah field Role
5. Verifikasi modal tetap terbuka
6. Verifikasi tidak ada request simpan yang terkirim

### TC-FA-SU-240: Submit dengan sebagian field kosong: pesan hanya untuk field yang kosong

7. Klik `[Clear Field]` untuk menghapus pesan error TC-FA-SU-239
8. Pilih Group Finance & Accounting lalu klik `[Submit]`
9. Verifikasi pesan "Transaction must not be empty" dan "Role must not be empty" saja
10. Verifikasi pesan Group tidak tampil
11. Pilih Transaction Disposal lalu klik `[Submit]`
12. Verifikasi pesan "Role must not be empty" saja

### TC-FA-SU-241: Clear Field mengosongkan Group, Transaction, dan Role tanpa menutup modal dan menghapus pesan error

13. Klik `[Clear Field]` untuk mengosongkan isian TC-FA-SU-240
14. Klik `[Submit]` kosong untuk memunculkan pesan error
15. Isi Group Finance & Accounting, Transaction Disposal, dan Role Asset Admin
16. Centang `Stay on this form after submitting`
17. Klik `[Clear Field]`
18. Verifikasi tombol Group berlabel `Select Group` (Group kosong)
19. Verifikasi field Transaction kosong dan terkunci lagi
20. Verifikasi field Role kosong dan terkunci lagi
21. Verifikasi pesan error hilang
22. Verifikasi modal tetap terbuka tanpa dialog `Unsaved Changes`
23. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang sesuai pilihan
24. Hapus centang `Stay on this form after submitting` lalu klik `[✕]` pada modal

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 7, 13 dan 24. `[Clear Field]` antar TC membersihkan error inline yang identik (R-12, S-09); modal ditutup tanpa dialog karena kosong.
- Modal Assign Transaction Role dibuka sekali di awal dan dipakai ketiga TC (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Langkah penghubung Search (S-03): Search nama pengguna target pada langkah 1 digabung ke langkah pembuka Detail atau pembacaan baris, untuk menemukan baris target di User List yang memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah berikutnya mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-241 langkah 3 dan 4 saling bertentangan: field sudah terisi lalu `[Submit]` "kosong" dipakai untuk memunculkan error; spec memicu error dengan `[Submit]` kosong terlebih dahulu, lalu mengisi field, mencentang Stay, dan `[Clear Field]`. Pesan error pada field terisi dapat sudah hilang saat `[Clear Field]` diklik sehingga klausa "pesan error hilang" tidak teruji kuat.
  - TC-FA-SU-239 butir b ("tidak ada request simpan") tidak menyebut cara observasi; spec menuliskannya sebagai Verifikasi sesuai teks TC.
  - TC-FA-SU-240 butir a menyebut pesan "saja" tanpa menyebut bahwa pesan Group tidak tampil; spec menambah satu Verifikasi absence pesan Group (anchor: pesan Transaction dan Role tampil) sebagai penjabaran kata "saja".
