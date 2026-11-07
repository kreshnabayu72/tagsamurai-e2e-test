---
id: TC-FA-SU-E2E-009-user-type-detail-user-admin-basic-dan-prioritas-bila-beririsan
title: "User Type Detail User: Admin, Basic, dan Prioritas Bila Beririsan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-26
  - TC-FA-SU-27
  - TC-FA-SU-28
coverage:
  web: automated
---

# User Type Detail User: Admin, Basic, dan Prioritas Bila Beririsan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan penugasan (#23): Lina Marlina (Total Control dengan Global Role aktif), Oscar Pranata (Group Manager dengan Group Role aktif), Gita Permata (Global Role Import Data dan Manage accounting), Hana Kusuma (tanpa Global Role maupun Group Role). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tidak ada selain pengamatan UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-26: User Type Detail User: Admin

1. Ketik Search `Gita Permata`, tekan Enter
2. Klik nama `Gita Permata`
3. Verifikasi badge User Type `Admin` pada General Information Gita Permata karena minimal satu Global Role aktif atau Group Role aktif dan bukan Total Control, Read Only, atau Group Manager
4. Verifikasi Transaction Role tidak dihitung dalam penentuan User Type Gita Permata
5. Klik segmen Breadcrumb `User`
6. Verifikasi User List termuat dengan baris `Gita Permata` tampil
7. Verifikasi User List tidak memuat kolom User Type
8. Klik `(←)` pada kotak Search

### TC-FA-SU-27: User Type Detail User: Basic

9. Ketik Search `Hana Kusuma`, tekan Enter
10. Klik nama `Hana Kusuma`
11. Verifikasi badge User Type `Basic` pada General Information Hana Kusuma karena tanpa Global Role maupun Group Role aktif
12. Verifikasi Transaction Role tidak dihitung dalam penentuan User Type Hana Kusuma
13. Klik segmen Breadcrumb `User`
14. Verifikasi User List termuat dengan baris `Hana Kusuma` tampil
15. Verifikasi User List tidak memuat kolom User Type
16. Klik `(←)` pada kotak Search

### TC-FA-SU-28: User Type prioritas bila beririsan: TC lebih tinggi dari RO, GM, Admin, Basic

17. Ketik Search `Lina Marlina`, tekan Enter
18. Klik nama `Lina Marlina`
19. Verifikasi badge User Type `Total Control` pada Lina Marlina walau memiliki Global Role aktif
20. Klik segmen Breadcrumb `User`
21. Ganti isi kotak search dengan `Oscar Pranata`, tekan Enter
22. Klik nama `Oscar Pranata`
23. Verifikasi badge User Type `Group Manager` (bukan `Admin`) pada Oscar Pranata walau memiliki Group Role aktif
24. Klik segmen Breadcrumb `User`
25. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
26. Klik nama `Gita Permata`
27. Verifikasi badge User Type `Admin` pada Gita Permata (Global Role aktif tanpa tier)
28. Klik segmen Breadcrumb `User`
29. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
30. Klik nama `Hana Kusuma`
31. Verifikasi badge User Type `Basic` pada Hana Kusuma (tanpa peran)
32. Klik segmen Breadcrumb `User`
33. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 9, 17, 21, 25, dan 29 (Search untuk menemukan baris target, R-16), langkah 5, 13, 20, 24, 28, dan 32 (kembali ke User List lewat Breadcrumb), langkah 8, 16, dan 33 (mengosongkan Search, S-09).
- Langkah 7 dan 15 mengasersi absence kolom User Type; anchor positifnya adalah Verifikasi langkah 6 dan 14 (User List termuat dengan baris pengguna hasil Search yang sama tampil sesudah kembali dari Detail), sesuai bagian 8b butir 2. Expected c TC-FA-SU-26 dan 27 hanya diasersi di blok masing-masing; blok TC-FA-SU-28 tidak mengulang asersi kolom User List karena Expected TC-FA-SU-28 tidak memuatnya.
- Pembagian TC lintas spec: User Type Total Control, Read Only, dan Group Manager (TC-FA-SU-23 sampai 25) ada di spec 008.
- Temuan untuk QA:
  - TC-FA-SU-26 dan 27 Expected b ("Transaction Role tidak dihitung dalam penentuan User Type") tidak menyebut Transaction Role pengguna yang dipakai sebagai pembeda; spec mengasersi kalimat Expected TC apa adanya.
  - TC-FA-SU-28 Expected a sampai c tidak menyebut pengguna acuan per butir selain Langkah Uji (Lina Marlina, Oscar Pranata, Gita Permata, Hana Kusuma); spec mengikuti urutan Langkah Uji.
  - Langkah Uji TC-FA-SU-28 ("Buka Detail ... dan Hana Kusuma") tidak merinci cara menemukan tiap baris; spec memakai Search.
