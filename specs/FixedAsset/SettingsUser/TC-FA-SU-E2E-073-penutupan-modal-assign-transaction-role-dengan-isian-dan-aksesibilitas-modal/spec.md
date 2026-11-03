---
id: TC-FA-SU-E2E-073-penutupan-modal-assign-transaction-role-dengan-isian-dan-aksesibilitas-modal
title: "Penutupan Modal Assign Transaction Role dengan Isian dan Aksesibilitas Modal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-242
  - TC-FA-SU-1046
coverage:
  web: automated
---

# Penutupan Modal Assign Transaction Role dengan Isian dan Aksesibilitas Modal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting).
- Data uji: Group Finance & Accounting dipilih pada TC-FA-SU-242; TC-FA-SU-1046 tidak memerlukan isian.
- Kemampuan teknis: pembacaan atribut ARIA elemen (`aria-required`, `aria-describedby`) dan urutan fokus keyboard pada halaman (disediakan tim FE).
- State global yang diubah: tidak ada data yang disimpan; isian modal dibuang lewat `[Leave]`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-242: Menutup modal dengan isian: dialog Unsaved Changes, Leave, Cancel, Esc, dan klik backdrop

1. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, pilih Group Finance & Accounting, lalu klik `[✕]`
2. Verifikasi dialog dengan Body "You have unsaved changes. Are you sure you want to leave?"
3. Verifikasi tombol `[Cancel]` dan `[Leave]`
4. Klik `[Cancel]`
5. Verifikasi modal kembali tampil dengan isian dipertahankan (Group Finance & Accounting)
6. Tekan Esc
7. Verifikasi dialog `Unsaved Changes` tampil
8. Klik `[Leave]`
9. Verifikasi modal menutup
10. Klik `[+ Assign]` untuk membuka modal baru lalu klik `[✕]`
11. Verifikasi modal kosong menutup langsung tanpa dialog
12. Klik `[+ Assign]` untuk membuka modal baru lalu klik backdrop
13. Verifikasi modal tidak menutup
14. Verifikasi tidak ada dialog yang muncul

### TC-FA-SU-1046: Aksesibilitas modal Assign Transaction Role: aria-required, aria-describedby, focus trap, dan keyboard

15. Verifikasi field Group, Transaction, dan Role memiliki `aria-required="true"`
16. Klik `[Submit]` tanpa mengisi apa pun
17. Verifikasi setiap field yang menampilkan pesan inline ("Group must not be empty", "Transaction must not be empty", "Role must not be empty") memiliki `aria-describedby` yang menunjuk ke pesan tersebut
18. Tekan Tab berulang dari field pertama
19. Verifikasi fokus keyboard terkunci di dalam modal (Tab dan Shift+Tab berputar di dalam modal)
20. Verifikasi field dapat dioperasikan dengan Tab dan Enter
21. Tekan Esc pada modal kosong
22. Verifikasi modal menutup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Modal yang dibuka di akhir TC-FA-SU-242 (untuk klik backdrop) dipakai TC-FA-SU-1046 tanpa dibuka ulang karena kosong dan tidak berubah (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-FA-SU-242 langkah 5 menyebut `[Leave]` lalu langkah 6 membuka modal baru; Expected c ("modal kosong menutup langsung") tidak punya langkah penutupan pada TC; spec menambahkan klik `[✕]` pada modal kosong sebagai pemicu asersi tersebut.
  - TC-FA-SU-1046 langkah 2 ("periksa atribut field") tidak menyebut cara pemeriksaan atribut; spec menuliskannya sebagai kemampuan "disediakan tim FE".
