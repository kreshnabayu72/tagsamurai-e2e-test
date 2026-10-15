---
id: TC-AUTH-LP-E2E-008-login-plan-parity
title: "Login Identik pada Entitas dengan Plan Starter, Growth, Professional, Enterprise, dan Custom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-76
coverage:
  web: automated
---

# Login Identik pada Entitas dengan Plan Starter, Growth, Professional, Enterprise, dan Custom

## Prerequisites

- Mode: FE+BE.
- Data Pre-setup bersama (tidak di-seed spec): lima user berstatus Activated dan Active, masing-masing dari entitas dengan plan berbeda. Entitas dan plan-nya disiapkan tim FE dan tidak dapat dibuat oleh spec karena tiap plan berada pada entitas terpisah. Spec hanya membaca (login lalu logout), tidak mengubah atau menghapus data user. Efek yang tersisa: tiap login menambah satu entri Activity Log Session pada entitas masing-masing; tidak dipulihkan.
- Environment variable: `LP_PASSWORD` (password awal kelima akun Pre-setup). Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis (fixture BE): tiap user device terpercaya, lokasi sama seperti login sebelumnya, pernah login dan logout kurang dari 30 hari lalu, dan versi Privacy Policy terakhir yang disetujui sama dengan versi aktif, sehingga tidak ada gate Agreement dan MFA; reCAPTCHA mode uji di environment.
- Pemulihan: sesi login ditutup lewat logout di akhir tiap akun; hook `after` menutup sesi yang tersisa bila spec gagal di tengah.
- TC-AUTH-LP-76: Tanpa login (guest); browser web
- TC-AUTH-LP-76: User `starter.user@qwertysystem.net` (entitas plan Starter), `growth.user@qwertysystem.net` (Growth), `professional.user@qwertysystem.net` (Professional), `enterprise.user@qwertysystem.net` (Enterprise), `custom.user@qwertysystem.net` (Custom), masing-masing Activated dan Active
- TC-AUTH-LP-76 data: Email: kelima alamat di atas (Pre-setup, tanpa suffix per run); Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-76: Login identik pada akun dari entitas dengan plan Starter, Growth, Professional, Enterprise, dan Custom

1. Buka halaman Login with Password
2. Verifikasi halaman Login with Password tampil dengan Title "Login with Password" dan tanpa Alert pesan server (akun plan Starter)
3. Isi field Email dengan "starter.user@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi login berhasil: browser menuju Portal — Product Hub
7. Verifikasi tidak ada pesan upsell, pembatasan, atau perbedaan perilaku untuk plan Starter
8. Logout dari Portal — Product Hub
9. Buka halaman Login with Password
10. Verifikasi halaman Login with Password tampil dengan Title "Login with Password" dan tanpa Alert pesan server (akun plan Growth)
11. Isi field Email dengan "growth.user@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
12. Selesaikan reCAPTCHA
13. Klik [Log in]
14. Verifikasi login berhasil: browser menuju Portal — Product Hub
15. Verifikasi tidak ada pesan upsell, pembatasan, atau perbedaan perilaku untuk plan Growth
16. Logout dari Portal — Product Hub
17. Buka halaman Login with Password
18. Verifikasi halaman Login with Password tampil dengan Title "Login with Password" dan tanpa Alert pesan server (akun plan Professional)
19. Isi field Email dengan "professional.user@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
20. Selesaikan reCAPTCHA
21. Klik [Log in]
22. Verifikasi login berhasil: browser menuju Portal — Product Hub
23. Verifikasi tidak ada pesan upsell, pembatasan, atau perbedaan perilaku untuk plan Professional
24. Logout dari Portal — Product Hub
25. Buka halaman Login with Password
26. Verifikasi halaman Login with Password tampil dengan Title "Login with Password" dan tanpa Alert pesan server (akun plan Enterprise)
27. Isi field Email dengan "enterprise.user@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
28. Selesaikan reCAPTCHA
29. Klik [Log in]
30. Verifikasi login berhasil: browser menuju Portal — Product Hub
31. Verifikasi tidak ada pesan upsell, pembatasan, atau perbedaan perilaku untuk plan Enterprise
32. Logout dari Portal — Product Hub
33. Buka halaman Login with Password
34. Verifikasi halaman Login with Password tampil dengan Title "Login with Password" dan tanpa Alert pesan server (akun plan Custom)
35. Isi field Email dengan "custom.user@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
36. Selesaikan reCAPTCHA
37. Klik [Log in]
38. Verifikasi login berhasil: browser menuju Portal — Product Hub
39. Verifikasi tidak ada pesan upsell, pembatasan, atau perbedaan perilaku untuk plan Custom
40. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah login diulang untuk tiap plan dengan akun yang berbeda; bukan spec Role Matrix karena yang dibandingkan adalah plan entitas, bukan role (bagian 3a konvensi tidak berlaku).
- Langkah penghubung (S-03): logout setelah tiap akun dan "Buka halaman Login with Password" untuk akun berikutnya; tanpa `Verifikasi`.
- Asersi "halaman Login with Password, validasi, dan pesan identik" (Expected butir a) dipecah per akun menjadi Verifikasi Title dan tidak adanya Alert sebelum login, ditambah Verifikasi login berhasil; tidak ada asersi baru di luar Expected TC.
- Email kelima akun memakai nilai Pre-setup tanpa suffix per run karena akun milik entitas per plan yang disiapkan tim FE, bukan data dinamis spec (S-12: data Pre-setup yang dipakai hanya-baca).
- Temuan untuk QA: TC-AUTH-LP-76 Expected butir a ("halaman Login with Password, validasi, dan pesan identik") tidak menyebut elemen atau pesan yang dibandingkan; spec memverifikasi Title dan tidak adanya Alert, dan cakupan perbandingan "validasi" perlu diperjelas.
- Jumlah langkah melewati ~35 (smell): satu topik (paritas login lintas plan entitas) dengan langkah identik per akun; tiap akun memulai dari halaman Login with Password dan logout, sehingga bagian sesudahnya tetap bermakna walau akun sebelumnya gagal.
