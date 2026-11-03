---
id: TC-FA-SU-E2E-005-sakelar-active-dan-menu-row-action-user-list
title: "Sakelar Active dan Menu Row Action User List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-13
  - TC-FA-SU-14
coverage:
  web: automated
---

# Sakelar Active dan Menu Row Action User List

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan Global Settings (#38): Rudi Hartono nonaktif di Global Settings (sakelar FAMS ON); status aktivasi Hana Kusuma dan Kartika Sari (Pending Activation), Indra Wijaya dan Lukman Hakim (Pending Email Confirmation) dari #37. Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: pembacaan tooltip hover pada sakelar Disabled.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Menu row action" (dipakai langkah 12 sampai 15):

| Baris | Status | Opsi menu (urut) |
|---|---|---|
| Hana Kusuma | belum aktivasi, Active | `Detail`, `Edit Home Group`, `Resend Activation Email` |
| Kartika Sari | belum aktivasi, Inactive | `Detail`, `Edit Home Group`, `Resend Activation Email` |
| Budi Santoso | sudah aktivasi, Active | `Detail`, `Edit Home Group` |
| Doni Prasetyo | sudah aktivasi, Inactive | `Detail`, `Edit Home Group` |
| Indra Wijaya | ubah email, Active | `Detail`, `Edit Home Group`, `Resend Confirmation Email` |

## Test Steps

### TC-FA-SU-13: Sakelar Active: ON, OFF, Disabled untuk Default User, Self, dan Global-inactive

1. Verifikasi pengguna Active (Budi Santoso) menampilkan sakelar ON berwarna primary Fixed Asset (biru)
2. Verifikasi pengguna Inactive (Doni Prasetyo) menampilkan sakelar OFF
3. Hover sakelar Ahmad Dahlan (Default User)
4. Verifikasi sakelar Ahmad Dahlan ON Disabled dengan tooltip `Default User cannot be modified.`
5. Klik halaman 2 pada pagination
6. Hover sakelar Lina Marlina (aktor sendiri)
7. Verifikasi sakelar Lina Marlina ON Disabled dengan tooltip `You can't manage your own account from here.`
8. Hover sakelar Rudi Hartono (nonaktif di Global Settings)
9. Verifikasi sakelar Rudi Hartono ON Disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
10. Verifikasi posisi ON pada sakelar Rudi Hartono dipertahankan
11. Klik halaman 1 pada pagination

### TC-FA-SU-14: Menu row action per kondisi status aktivasi dan Active

12. Untuk setiap baris pada tabel "Menu row action" (langkah 12 sampai 15): klik `⋯` pada kolom Actions baris itu
13. Verifikasi opsi menu dan urutannya sama dengan kolom "Opsi menu (urut)" baris itu
14. Verifikasi menu tidak memuat row action Activate atau Deactivate
15. Tutup menu dengan Esc
16. Klik halaman 2 pada pagination
17. Klik `⋯` pada kolom Actions baris Lukman Hakim (ubah email, Inactive)
18. Verifikasi opsi menu `Detail`, `Edit Home Group`, `Resend Confirmation Email` dalam urutan itu
19. Verifikasi menu tidak memuat row action Activate atau Deactivate
20. Tutup menu dengan Esc
21. Klik halaman 1 pada pagination

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 11, 16, dan 21 (pindah halaman pagination supaya baris yang diasersi tampil, S-14), langkah 15 dan 20 (menutup menu, S-09). Langkah 12 sampai 15 diulang untuk lima baris tabel parameter (ekspansi 20 langkah); Lukman Hakim berada di halaman 2 sehingga ditulis terpisah pada langkah 17 sampai 20.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (37 langkah). Seluruhnya satu kelas (screening tampilan baris User List, satu akun, tanpa mengubah data) dan dua blok TC berdiri sendiri.
- Pembagian TC lintas spec: TC-FA-SU-15 (menu row action Default User dan Self) ada di spec 016; TC-FA-SU-16 (pengguna baru tanpa role) ada di spec 015.
- Temuan untuk QA:
  - TC-FA-SU-14 Expected d menulis "urutan dark dulu" yang tidak bermakna; spec mengasersi urutan opsi menu persis seperti Expected a sampai c.
  - TC-FA-SU-13 Expected a menyebut warna primary Fixed Asset (biru) tanpa nilai warna; spec mengasersi sakelar ON berwarna primary Fixed Asset.
