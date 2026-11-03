---
id: TC-GS-NLU-E2E-014-create-screening-popup-aksesibilitas-hover-dan-saving-state-submit
title: "Create: screening Popup, aksesibilitas, hover dan Saving state Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-53
  - TC-GS-NLU-54
  - TC-GS-NLU-55
coverage:
  web: automated
---

# Create: screening Popup, aksesibilitas, hover dan Saving state Submit

## Prerequisites

- Mode: FE+BE (backend nyata; penahanan respons pada TC-GS-NLU-55 hanya untuk mengamati Saving state dan bukan kegagalan yang dipaksakan).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Position, Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By), Custom Field dasar. Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis: Non-Login User TC-GS-NLU-55: First Name `Ratna`, Last Name `Dewi`, Email `ratnadewi+{runId}-014@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-014` lewat API (mekanisme disediakan tim FE/BE).
- Kebutuhan intercept (`Spectra.intercept()`) untuk TC-GS-NLU-55: respons simpan Create ditahan sampai dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script. Hook `after` melepas intercept walau spec gagal di tengah.
- Kemampuan teknis: hover elemen; membaca atribut `aria-required`, `aria-describedby` dan posisi fokus; membaca state hover dan Saving state tombol.
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-53: Screening Popup Create Non-Login User

1. Klik `[+ Non-Login User]`
2. Verifikasi Header Popup: Title `Create Non-Login User`
3. Verifikasi Header Popup: tombol close `✕` di kanan atas
4. Verifikasi Body: Avatar upload bulat (Photo) berada paling atas
5. Verifikasi Body: `First Name*` placeholder `Enter first name`
6. Verifikasi Body: `Last Name*` placeholder `Enter last name`
7. Verifikasi Body: `Position` placeholder `Select position`
8. Verifikasi Body: `Division*` placeholder `Select division`
9. Verifikasi Body: `Employee ID` placeholder `Enter employee ID`
10. Verifikasi Body: `Email*` placeholder `Enter email` dengan helper text `Used to send the activation email if this person is later converted to a login user.`
11. Verifikasi Body: `Represented By*` berisi button `[+ Select User]`
12. Verifikasi Body: Checkbox `Set as Temporary User` tidak tercentang dan field `Temporary Until` belum tampil
13. Verifikasi Body: pemisah diikuti bagian Custom Fields (Blood Type, Emergency Phone, Badge Note)
14. Verifikasi Footer: Checkbox `Stay on this form after submitting` tidak tercentang
15. Verifikasi Footer: Tombol `[Clear Field]`
16. Verifikasi Footer: Tombol `[Submit]`

### TC-GS-NLU-54: Aksesibilitas Popup Create: atribut field wajib dan focus trap

17. Verifikasi field First Name, Last Name, Division, Email, dan tombol Represented By memiliki `aria-required="true"`
18. Tekan Tab berulang dari field pertama sampai melewati `[Submit]`
19. Verifikasi fokus tetap berputar di dalam popup (focus trap) dan tidak keluar ke halaman di belakang
20. Kosongkan First Name, lalu klik `[Submit]`
21. Verifikasi field First Name yang error memiliki `aria-describedby` menunjuk pesan error `First name must not be empty`
22. Klik `✕`

### TC-GS-NLU-55: Hover dan Saving state tombol Submit pada Popup Create

23. Klik `[+ Non-Login User]`
24. Isi First Name `Ratna` dan Last Name `Dewi`
25. Pilih Division `Logistics`
26. Isi Email `ratnadewi+{runId}-014@qwertysystem.net`
27. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
28. Hover `[Submit]`
29. Verifikasi tombol `[Submit]` menampilkan state hover sesuai desain
30. Pasang intercept yang menahan respons simpan Create (network throttle)
31. Klik `[Submit]`
32. Verifikasi tombol `[Submit]` menampilkan indikator loading (Saving state)
33. Verifikasi tombol `[Submit]` non-interaktif (Saving state)
34. Lepas tahanan respons
35. Verifikasi tombol `[Submit]` keluar dari Saving state setelah response diterima

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti nomor TC; TC-GS-NLU-54 dan TC-GS-NLU-55 sama-sama bukan validasi submit sukses sehingga TC-GS-NLU-55 yang berujung record baru ada di akhir (S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 22 (menutup popup yang nilainya tidak berubah dibanding snapshot saat dibuka, sehingga tertutup tanpa dialog `Unsaved Changes`; TC-GS-NLU-91 menyatakan perilaku itu), langkah 30 dan 34 (pasang dan lepas intercept).
- Langkah 2 sampai 16 memetakan butir Expected TC-GS-NLU-53 a, b, dan c satu per klausa (S-01). Langkah 17, 19, dan 21 memetakan Expected a, b, dan c TC-GS-NLU-54. Langkah 29, 32, 33, 35 memetakan Expected a dan b TC-GS-NLU-55; Saving state "loading dan non-interaktif" dipecah dua klausa.
- Temuan untuk QA:
  - TC-GS-NLU-55 Expected a hanya menyebut "state hover sesuai desain" tanpa nilai konkret (warna, kursor); spec mengasersi state hover tombol dan nilai pembandingnya ditentukan di tahap script.
  - TC-GS-NLU-55 langkah 8 menyebut "network throttle" tanpa durasi atau endpoint; spec menahan respons sampai dilepas lewat langkah 34. Expected b ("sampai response diterima") diasersi lewat langkah 35.
  - TC-GS-NLU-54 langkah 4 menyebut "Kosongkan First Name" padahal field itu sudah kosong sejak popup dibuka; spec tetap mengosongkan field (tanpa efek) sesuai TC.
  - Email `ratnadewi@qwertysystem.net` pada TC-GS-NLU-55 diberi suffix `+{runId}-014` (S-12) karena record benar-benar tersimpan.
  - Post Condition TC-GS-NLU-53 sampai 55 berupa `-` sehingga tidak ada yang diasersi.
