---
id: TC-GS-UCF-E2E-011-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca Tabel Custom Field: Loading State, Loading saat Search atau Pagination, dan Error Load dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-7
  - TC-GS-UCF-8
  - TC-GS-UCF-11
coverage:
  web: automated
---

# Resilience Baca Tabel Custom Field: Loading State, Loading saat Search atau Pagination, dan Error Load dengan Try Again

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Tidak ada data yang di-seed atau dibuat di backend.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Kebutuhan mock (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit. Endpoint yang dipanggil halaman pada kondisi tes:
  - List Custom Field tab (rujukan `global-settings/custom-field-user/API/low-level-design.md` `/list` dan `openapi.yaml` modul; path dan `operationId` persis dilengkapi tim FE dari `openapi.yaml`, tidak disalin di spec ini): dipakai langkah 1 sampai 33. Respons mock memuat `{ data, totalRecords }`.
  - Modul ini tidak mengirim event SSE dan List tidak auto-refresh terhadap perubahan admin lain (PRD `custom-field-user.md` bagian Sync), sehingga tidak ada stream SSE yang perlu disediakan.
  - API pendukung di luar sumber modul (identitas pengguna, menu, flag Guided Tooltip, serta list User untuk sub-tab User List): disediakan tim FE, tanpa asersi.
  - Respons list normal (fixture baru `Fixture.customFieldUser.mockList011`): 14 field (6 Pre-setup dan 8 Population: `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date`, `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`), `totalRecords` 14, halaman 1 berisi 10 baris. Dipakai langkah 1 sampai 9 (TC-GS-UCF-7) dan 31 sampai 33 (TC-GS-UCF-11).
  - Respons list dengan Search `phone` (langkah 10 sampai 24, TC-GS-UCF-8): `totalRecords` 12 dengan 10 baris pada halaman 1 dan 2 baris pada halaman 2, supaya tombol Next Pagination aktif setelah Search; ditahan 3 detik lalu dijawab normal untuk kedua permintaan (Search dan Next).
  - Respons list, jawab 500 (langkah 26 sampai 30, TC-GS-UCF-11). Intercept 500 dilepas dan diganti respons normal pada langkah 31 sebelum `[Try Again]`.
  - Payload sesi dan izin Total Control (capability "Manage user and role" penuh) disediakan tim FE sebagai API pendukung supaya tab Custom Field tampil.
  - Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true (lihat `suite.md`); pada mode mock nilai flag itu bagian dari API pendukung yang disediakan tim FE, supaya tab Custom Field tampil tanpa walkthrough yang menutupi layar.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.
- Suite berjalan serial (`parallel: false`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > User pada sub-tab User List (precondition TC-GS-UCF-7 dan 11); pembukaan tab Custom Field adalah aksi yang diuji sehingga ditulis di `## Test Steps`.

## Test Steps

### TC-GS-UCF-7: Loading state saat tabel memuat data

1. Pasang intercept pada respons list Custom Field: tahan 3 detik lalu jawab normal (14 field)
2. Klik tab Custom Field
3. Verifikasi komponen loading tampil di area tabel selama respons tertunda
4. Verifikasi tidak ada empty state selama respons tertunda
5. Verifikasi tidak ada pesan error selama respons tertunda
6. Tunggu respons diterima
7. Verifikasi komponen loading hilang
8. Verifikasi baris tabel tampil
9. Lepas intercept respons list Custom Field

### TC-GS-UCF-8: Loading state saat tabel dimuat ulang oleh Search atau Pagination

10. Pasang intercept pada respons list Custom Field: tahan 3 detik lalu jawab normal (Search `phone`: `totalRecords` 12)
11. Ketik Search `phone`, tekan Enter
12. Verifikasi komponen loading tampil di area tabel selama respons Search tertunda
13. Verifikasi Search `phone` tetap terlihat
14. Verifikasi state Pagination tetap terlihat
15. Tunggu respons diterima
16. Verifikasi hasil Search tampil
17. Klik Next pada Pagination
18. Verifikasi komponen loading tampil di area tabel selama respons Pagination tertunda
19. Verifikasi Search `phone` tetap terlihat
20. Verifikasi state Pagination tetap terlihat
21. Tunggu respons diterima
22. Verifikasi hasil halaman 2 tampil
23. Lepas intercept respons list Custom Field
24. Klik `(←)` pada kotak Search

### TC-GS-UCF-11: Error load tabel menampilkan pesan dengan `[Try Again]` dan pulih setelah dicoba ulang

25. Klik tab User List (kembali ke precondition: sub-tab Login User)
26. Pasang intercept pada respons list Custom Field: jawab 500
27. Klik tab Custom Field
28. Verifikasi `Unable to load this data.` tampil
29. Verifikasi tombol `[Try Again]` tampil
30. Verifikasi empty state `No custom fields yet` tidak tampil
31. Lepas intercept 500 dan pasang respons list Custom Field normal (14 field)
32. Klik `[Try Again]`
33. Verifikasi tabel memuat 14 field (`totalRecords` 14; 10 baris pada halaman 1)

## Notes

- Mode: mock (seluruh API di-mock, konvensi bagian 6). Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi yang menyangkut state backend nyata tidak teruji pada mode mock: spec ini hanya menguji rendering FE terhadap respons list yang dipaksa; baris yang tampil pada langkah 8, 16, 22, dan 33 berasal dari respons mock, bukan dari data backend. Asersi readback respons mock ditulis karena Expected TC memintanya (hasil tampil, tabel memuat), bukan diturunkan dari Post Condition.
- Loading state pada langkah 3 sampai 5, 12 sampai 14, dan 18 sampai 20 diasersi sebelum respons diterima (langkah 6, 15, 21), sebelum langkah yang mengubah state-nya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 15, dan 21 (menunggu respons), langkah 9 dan 23 (melepas intercept), langkah 24 (`(←)` menutup Search dan mereset tabel), langkah 25 (kembali ke sub-tab User List sebagai precondition TC-GS-UCF-11), dan langkah 31 (mengganti respons 500 dengan respons normal sebelum `[Try Again]`).
- Langkah 30 (empty state tidak tampil) beranchor langkah 28 dan 29 yang membuktikan pesan error tampil pada area tabel yang sama.
- Pembagian TC lintas spec: kegagalan tulis (Create, Edit) ada di spec 030; kegagalan hapus dan toggle di spec 049; kegagalan download di spec 060. Kelas b (fault injection) dipisah dari spec fungsional tabel utama.
- Temuan untuk QA:
  - TC-GS-UCF-8 mengklik Next setelah Search `phone`, sedangkan pada data Pre-setup dan Population hasil `phone` hanya `Office Phone` dan `Emergency Phone` (satu halaman) sehingga Next tidak aktif pada backend nyata; spec memakai respons mock `totalRecords` 12 supaya Next aktif. Perlu konfirmasi QA terhadap urutan Search lalu Next.
  - TC-GS-UCF-11 Expected b menulis "tabel memuat 14 baris" sedangkan Pagination default 10 per halaman; spec mengasersi `totalRecords` 14 dengan 10 baris pada halaman 1.
  - TC-GS-UCF-7 dan 8 menahan respons "3 detik" (nilai ditandai `PRD?` di TC); spec memakai 3 detik sebagai penahanan respons lewat intercept.
  - Path dan `operationId` endpoint list tidak disebut TC maupun PRD; spec merujuk LLD `/list` dan menyerahkan path persis ke tim FE (tidak diisi di sini, S-13).
