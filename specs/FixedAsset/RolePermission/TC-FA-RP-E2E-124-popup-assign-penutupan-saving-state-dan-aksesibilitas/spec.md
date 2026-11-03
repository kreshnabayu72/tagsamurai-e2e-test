---
id: TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas
title: "Popup Assign: penutupan, Saving state, dan aksesibilitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-421
  - TC-FA-RP-422
  - TC-FA-RP-423
  - TC-FA-RP-424
  - TC-FA-RP-425
coverage:
  web: automated
---

# Popup Assign: penutupan, Saving state, dan aksesibilitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menahan respons submit Assign lewat `Spectra.intercept()` di atas backend nyata agar state Saving teramati (menahan respons untuk mengamati state UI, bukan kegagalan yang dipaksa); intercept dilepas segera sesudah asersi (langkah 29). Membaca atribut ARIA elemen popup.
- State yang diubah dan pemulihannya: pada TC-FA-RP-424 Ahmad Fauzi ditetapkan Total Control saat respons dilepas. Hook `after` memulihkan kolam Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-421: Popup Assign ditutup lewat `[Cancel]` membuang seleksi tanpa dialog

1. Klik `[+ Assign]` di Tab `Total Control`
2. Centang Ahmad Fauzi
3. Klik `[Cancel]`
4. Verifikasi tidak ada toast
5. Verifikasi popup tertutup
6. Verifikasi dialog Unsaved Changes tidak tampil
7. Klik `[+ Assign]` di Tab `Total Control`
8. Verifikasi popup baru terbuka tanpa seleksi

### TC-FA-RP-422: Popup Assign ditutup lewat tombol Esc membuang seleksi tanpa dialog

9. Klik `[Cancel]` pada popup yang terbuka
10. Klik `[+ Assign]` di Tab `Total Control`
11. Centang Ahmad Fauzi
12. Tekan tombol Esc
13. Verifikasi popup tertutup
14. Verifikasi dialog Unsaved Changes tidak tampil
15. Klik `[+ Assign]` di Tab `Total Control`
16. Verifikasi seleksi dibuang (tidak ada user tercentang)

### TC-FA-RP-423: Klik backdrop di luar popup Assign tidak menutup popup

17. Centang Ahmad Fauzi
18. Klik area gelap di luar popup
19. Verifikasi popup tetap terbuka
20. Verifikasi seleksi Ahmad Fauzi dipertahankan
21. Verifikasi dialog tidak tampil
22. Klik `[Cancel]`

### TC-FA-RP-424: Tombol `[Assign]` memasuki Saving state saat submit diproses

23. Klik `[+ Assign]` di Tab `Total Control`
24. Centang Ahmad Fauzi
25. Tahan respons submit Assign lewat intercept
26. Klik `[Assign]`
27. Verifikasi tombol `[Assign]` berada pada Saving state (loading dan tidak dapat diklik ulang)
28. Lepas tahanan respons submit
29. Tunggu aksi selesai (popup tertutup)

### TC-FA-RP-425: Accessibility popup Assign Group Manager, field Group wajib, focus trap, dan Esc

30. Klik Tab `Group Manager`
31. Klik `[+ Assign]` di Tab `Group Manager`
32. Tekan Tab berulang melewati seluruh elemen popup
33. Verifikasi fokus tidak keluar dari popup (focus trapped)
34. Klik `[Assign]` tanpa memilih group agar pesan error field Group tampil
35. Verifikasi field Group memiliki `aria-required`
36. Verifikasi pesan error field Group memiliki `aria-describedby`
37. Tekan Esc
38. Verifikasi Esc menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 (menutup popup yang dibuka ulang pada langkah 7), langkah 22 (menutup popup), langkah 29 (tunggu aksi selesai sesudah melepas tahanan respons), langkah 34 (memunculkan pesan error field Group karena TC tidak menyebut kapan pesan itu ada, lihat Temuan untuk QA). Langkah 1 TC-FA-RP-423 (membuka popup) terpenuhi oleh langkah 15 karena popup yang dibuka di sana dipakai sebagai keadaan awal TC-FA-RP-423.
- Asersi absence toast pada langkah 4 diletakkan segera setelah pemicu `[Cancel]` (bagian 8b butir 11); popup tertutup (langkah 5) menjadi anchor artefak.
- Menahan respons submit pada TC-FA-RP-424 hanya mengamati state Saving (bukan kegagalan yang dipaksa), sehingga spec tetap berkelas fungsional.
- Alasan di atas sekitar 35 langkah (38 langkah): lima TC satu topik (perilaku popup Assign: penutupan, Saving state, aksesibilitas) pada popup yang sama; popup yang dibuka di akhir satu TC dipakai sebagai keadaan awal TC berikutnya, sehingga memecahnya berarti mengulang pembukaan popup dan seleksi. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-425 butir b menyebut "pesan error memiliki `aria-describedby`" tanpa menyebut aksi yang memunculkan pesan error; spec menambah langkah 34 (klik `[Assign]` tanpa memilih group).
  - TC-FA-RP-424 tidak menyebut hasil setelah respons dilepas; tidak diasersi.
