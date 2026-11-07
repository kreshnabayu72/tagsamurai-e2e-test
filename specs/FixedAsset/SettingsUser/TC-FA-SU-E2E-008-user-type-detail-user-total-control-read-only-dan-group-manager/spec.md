---
id: TC-FA-SU-E2E-008-user-type-detail-user-total-control-read-only-dan-group-manager
title: "User Type Detail User: Total Control, Read Only, dan Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-23
  - TC-FA-SU-24
  - TC-FA-SU-25
coverage:
  web: automated
---

# User Type Detail User: Total Control, Read Only, dan Group Manager

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan penugasan tier (#23): Lina Marlina (Total Control), Citra Lestari (Read Only), Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-23: User Type Detail User: Total Control

1. Ketik Search `Lina Marlina`, tekan Enter
2. Klik nama `Lina Marlina`
3. Verifikasi badge User Type `Total Control` pada General Information Lina Marlina karena tingkat akses Total Control
4. Verifikasi Transaction Role tidak dihitung dalam penentuan User Type Lina Marlina
5. Klik segmen Breadcrumb `User`
6. Verifikasi User List termuat dengan baris `Lina Marlina` tampil
7. Verifikasi User List tidak memuat kolom User Type
8. Klik `(←)` pada kotak Search

### TC-FA-SU-24: User Type Detail User: Read Only

9. Ketik Search `Citra Lestari`, tekan Enter
10. Klik nama `Citra Lestari`
11. Verifikasi badge User Type `Read Only` pada General Information Citra Lestari karena tingkat akses Read Only
12. Verifikasi Transaction Role tidak dihitung dalam penentuan User Type Citra Lestari
13. Klik segmen Breadcrumb `User`
14. Verifikasi User List termuat dengan baris `Citra Lestari` tampil
15. Verifikasi User List tidak memuat kolom User Type
16. Klik `(←)` pada kotak Search

### TC-FA-SU-25: User Type Detail User: Group Manager

17. Ketik Search `Oscar Pranata`, tekan Enter
18. Klik nama `Oscar Pranata`
19. Verifikasi badge User Type `Group Manager` pada General Information Oscar Pranata karena Group Manager pada IT Infrastructure tanpa tingkat akses
20. Verifikasi Transaction Role tidak dihitung dalam penentuan User Type Oscar Pranata
21. Klik segmen Breadcrumb `User`
22. Verifikasi User List termuat dengan baris `Oscar Pranata` tampil
23. Verifikasi User List tidak memuat kolom User Type
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 9, dan 17 (Search untuk menemukan baris target, R-16), langkah 5, 13, dan 21 (kembali ke User List lewat Breadcrumb), langkah 8, 16, dan 24 (mengosongkan Search sebelum TC berikutnya, S-09).
- Langkah 7, 15, dan 23 mengasersi absence kolom User Type; anchor positifnya adalah Verifikasi langkah 6, 14, dan 22 (User List termuat dengan baris pengguna hasil Search yang sama tampil sesudah kembali dari Detail), sesuai bagian 8b butir 2.
- Pembagian TC lintas spec: User Type Admin, Basic, dan prioritas bila beririsan (TC-FA-SU-26 sampai 28) ada di spec 009.
- Temuan untuk QA:
  - TC-FA-SU-23 sampai 25 Expected b ("Transaction Role tidak dihitung dalam penentuan User Type") tidak menyebut Transaction Role pengguna yang dipakai sebagai pembeda; Pre-setup #39 hanya memberi Transaction Role untuk Lina Marlina, Mira Anggraini, dan Yuda Pratama. Spec mengasersi kalimat Expected TC apa adanya.
  - TC-FA-SU-23 sampai 25 Expected c ("User Type hanya muncul di Detail User dan bukan kolom User List") diasersi sesudah kembali ke User List; kolom User List mengacu ke daftar kolom pada TC-FA-SU-1.
