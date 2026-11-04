---
id: TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes
title: "Create: penutupan Popup, [Clear Field], backdrop, dan Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-139
  - TC-GS-USER-140
  - TC-GS-USER-141
  - TC-GS-USER-142
  - TC-GS-USER-143
  - TC-GS-USER-1005
  - TC-GS-USER-1062
coverage:
  web: automated
---

# Create: penutupan Popup, [Clear Field], backdrop, dan Unsaved Changes

## Prerequisites

- Mode: mock.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2). Pada mode mock sesi aktor dipasang hook `before` sebagai sesi mock tanpa login ke backend nyata (mekanisme disediakan tim FE); hook `after` memulihkan sesi ke akun default suite.
- Env var: tidak ada (tidak ada login ke backend nyata, tidak ada password).
- Layar awal: hook `beforeEach` mengembalikan layar ke Global Settings > User > User List, sub-tab Login User.
- Kebutuhan mock (seluruh API di-mock; API yang di-mock mengacu `global-settings/user/API/user-crud.yaml`; API pendukung disediakan tim FE):
  | method path (yaml:baris) | respons dipaksa |
  |---|---|
  | `POST /v2/iam/users/list` (11) | daftar User Login, sedikitnya satu baris tetap |
  | `POST /v2/iam/users` (334) | Create; dipantau tanpa dijawab, nol request |

  Sumber opsi dropdown Division, Access, dan Position form Create disediakan tim FE.

  Rincian respons:
  - Respons daftar User Login: sedikitnya satu baris, jumlah baris tetap selama spec.
  - Respons opsi form Create: Division (`Finance`), opsi Access (`Fixed Asset`), dan Position; Custom Field aktif tidak diperlukan.
  - Endpoint Create user dipantau tanpa dijawab dan harus menerima nol request selama spec ini.
- Data Pre-setup (nilai mock, tidak ada data tercipta): Division `Finance` (No. 23); opsi Access `Fixed Asset` (No. 26).
- Data Dinamis: tidak ada; spec ini tidak membuat data.
- Cleanup: tidak ada data yang dibuat; hook `beforeEach` menutup Popup atau dialog yang terbuka.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Catat baseline jumlah baris User List

### TC-GS-USER-139: [Clear Field] mengosongkan seluruh field tanpa dialog

2. Klik `[+ User]` di Table Tools
3. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso@qwertysystem.net`, pilih Access `Fixed Asset`
4. Centang `Stay on this form after submitting`
5. Klik `[Clear Field]`
6. Verifikasi First Name kosong dan menampilkan placeholder
7. Verifikasi Last Name kosong dan menampilkan placeholder
8. Verifikasi Division kosong dan menampilkan placeholder
9. Verifikasi Email kosong dan menampilkan placeholder
10. Verifikasi Access (multi dropdown) kosong dan menampilkan placeholder `Select access`
11. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
12. Verifikasi tidak ada dialog konfirmasi

### TC-GS-USER-1005: Klik backdrop saat form terisi tidak menutup Popup

13. Isi First Name `Budi`
14. Klik area backdrop di luar Popup
15. Verifikasi Popup Create tetap terbuka
16. Verifikasi First Name tetap `Budi`
17. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-USER-141: Tutup Popup terisi via [✕] memunculkan dialog Unsaved Changes

18. Klik `✕`
19. Verifikasi dialog Title `Unsaved Changes` dengan severity warning
20. Verifikasi body dialog `You have unsaved changes. Are you sure you want to leave?`
21. Verifikasi tombol `[Cancel]` dengan variant text dan severity contrast
22. Verifikasi tombol `[Leave]` dengan variant filled dan severity warning
23. Klik `[Cancel]`

### TC-GS-USER-143: Dialog Unsaved Changes [Cancel] kembali ke form dengan input utuh

24. Tekan `Esc`
25. Verifikasi dialog Unsaved Changes muncul
26. Klik `[Cancel]`
27. Verifikasi dialog Unsaved Changes tertutup
28. Verifikasi Popup Create tetap terbuka
29. Verifikasi First Name tetap `Budi`

### TC-GS-USER-142: Dialog Unsaved Changes [Leave] menutup Popup dan membuang input

30. Klik `✕`
31. Klik `[Leave]`
32. Verifikasi Popup Create tertutup
33. Verifikasi jumlah baris User List sama dengan baseline
34. Verifikasi tidak ada request ke endpoint Create user
35. Klik `[+ User]` di Table Tools
36. Verifikasi Popup Create baru terbuka
37. Verifikasi seluruh field Popup Create baru kosong dan menampilkan placeholder

### TC-GS-USER-140: Tutup Popup kosong via [✕] tanpa dialog

38. Klik `✕` tanpa mengisi apa pun
39. Verifikasi Popup Create langsung tertutup
40. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-USER-1062: Field diisi lalu dikosongkan kembali, tutup Popup tanpa dialog

41. Klik `[+ User]` di Table Tools
42. Isi First Name `Budi`
43. Hapus seluruh isi First Name sampai kosong
44. Klik `✕`
45. Verifikasi Popup Create langsung tertutup
46. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Mode: mock. Seluruh API di-mock karena yang diuji hanya perilaku penutupan, `[Clear Field]`, backdrop, dan dialog di sisi UI; tidak ada Submit yang berhasil dan tidak ada data tercipta.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (46 langkah) karena seluruh TC berada di satu kelas (penutupan dan pengosongan form), satu layar (Popup Create), dan satu pembukaan form dipakai bersama oleh lima TC pertama. Tiap blok mengamati kejadian tutup atau kosong yang berbeda dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan form dilakukan tiga kali (langkah 2, 35, dan 41) sesuai tiga kejadian penutupan form (langkah 31, 38, dan 44).
- Urutan TC sumber diubah: TC-GS-USER-139 (kosongkan form) dan TC-GS-USER-1005 (backdrop) berada di awal karena tidak menutup form; TC-GS-USER-141 dan TC-GS-USER-143 memakai form yang sama dengan First Name `Budi` dan kembali ke form lewat `[Cancel]`; TC-GS-USER-142 menutup form dirty dengan `[Leave]`, lalu Popup baru dari TC-GS-USER-142 dipakai untuk TC-GS-USER-140 (menutup form bersih, bagian 3 prinsip 6); TC-GS-USER-1062 terakhir karena butuh form baru. Form yang sudah diisi lalu dikosongkan lewat `[Clear Field]` tidak dipakai sebagai form bersih.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline jumlah baris User List untuk asersi "tidak ada user dibuat" pada TC-GS-USER-142), 23 (klik `[Cancel]` agar form kembali setelah dialog TC-GS-USER-141 diamati, state awal TC-GS-USER-143).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 34 (tidak ada request Create) memperkuat "tidak ada user dibuat" TC-GS-USER-142 dengan padanan di sisi mock.
- Langkah 6 sampai 10 memverifikasi lima field yang diisi pada langkah 3 satu per satu karena field kosong akibat `[Clear Field]` dipecah per field (S-01); field lain tidak diisi pada langkah 3.
- Temuan untuk QA:
  - TC-GS-USER-139 Expected a "Semua field kembali kosong" tidak mendaftar field; spec memverifikasi kelima field yang diisi.
  - TC-GS-USER-1005 dan TC-GS-USER-1062 mengutip `prd-conventions.md` §24.1c; TC-GS-USER-1005 tidak menyebut cara klik backdrop (posisi klik di luar Popup); spec mengklik area backdrop di luar Popup.
  - TC-GS-USER-141 Expected c menyebut warna sebagai `severity`/`variant` komponen (`text`, `contrast`, `filled`, `warning`); spec mengasersi atribut komponen, bukan warna piksel.
  - TC-GS-USER-139, 141, 142, 143, 1005, 1062 memakai data `Budi Santoso` tanpa suffix; karena tidak ada data tercipta, spec tidak menambah suffix pada nilai yang diketik.
  - Sumber opsi dropdown form tidak disebut di TC dan PRD; endpoint `POST /v2/iam/users/options` adalah opsi filter User List, bukan sumber dropdown form, sehingga tidak dipakai di spec ini dan sumber opsi disediakan tim FE (inferensi, diterima 2026-11-03; temuan sumber untuk pemilik PRD §4.1.3).
