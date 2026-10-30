---
id: TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss
title: "Guided Tooltip Tab Custom Field: Muncul Otomatis pada Kunjungan Pertama, Skip, Klik Overlay, Done, dan Esc Menandai Seen, serta Replay lewat Tombol [?]"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-23
  - TC-GS-UCF-24
  - TC-GS-UCF-25
  - TC-GS-UCF-401
  - TC-GS-UCF-402
coverage:
  web: automated
---

# Guided Tooltip Tab Custom Field: Muncul Otomatis pada Kunjungan Pertama, Skip, Klik Overlay, Done, dan Esc Menandai Seen, serta Replay lewat Tombol [?]

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor (urutan pemakaian dalam spec; password tidak ditulis di spec atau fixture):

| TC | Akun | Email (Pre-setup) | Env var password |
|---|---|---|---|
| TC-GS-UCF-25 | Total Control (Sari Dewi), flag seen sudah true | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-UCF-23 | Total Control Client A (First Visit A, Gita Anjani) | `totalControlFirstVisitA_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FVA_TC_PASSWORD` (env baru) |
| TC-GS-UCF-24 | Total Control Client A (First Visit B, Hadi Prasetyo) | `totalControlFirstVisitB_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FVB_TC_PASSWORD` (env baru) |
| TC-GS-UCF-401 | Total Control Client A (First Visit D, Kartika Pertiwi) | `totalControlFirstVisitD_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FVD_TC_PASSWORD` (env baru) |
| TC-GS-UCF-402 | Total Control Client A (First Visit E, Lukman Hakim) | `totalControlFirstVisitE_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FVE_TC_PASSWORD` (env baru) |

  Env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Akun Total Control login di hook `before`; akun First Visit login lewat langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field untuk akun Total Control (TC-GS-UCF-25). Untuk akun First Visit, kunjungan pertama ke tab Custom Field adalah pemicu auto-open sehingga pembukaan tab ditulis di `## Test Steps`.
- Guided Tooltip (page_key `gs-custom-field-user`): spec ini menguji flag `guided_tooltip_seen_gs-custom-field-user` sendiri, sehingga dikecualikan dari penyetelan true oleh hook suite `before` untuk akun First Visit A, B, D, dan E (lihat `suite.md`). Hook `before` mencatat nilai awal flag tiap akun First Visit lalu mereset flag ke belum ada (precondition TC-GS-UCF-23, 24, 401, dan 402); akun Total Control memakai flag true dari hook suite (precondition TC-GS-UCF-25). Hook `after` memulihkan nilai awal flag semua akun yang disentuh. Mekanisme baca, reset, penyetelan, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Data: tidak ada Data Pre-setup yang diasersi dan tidak ada Data Dinamis.
- Kemampuan teknis: klik pada area overlay gelap di luar tooltip box (koordinat di luar spotlight dan tooltip box); tombol Esc; hover; muat ulang halaman (tidak ada form terbuka sehingga tidak ada dialog `beforeunload`); ganti akun (logout lalu login).
- State global: flag Guided Tooltip akun First Visit A, B, D, dan E (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-25: Tombol [?] memulai ulang walkthrough tanpa mereset flag

1. Arahkan kursor ke `[?]` di sebelah kanan Breadcrumb
2. Verifikasi tooltip `Show guide` tampil
3. Klik `[?]`
4. Verifikasi walkthrough mulai dari Step 1
5. Klik `[Next]`
6. Klik `[Back]`
7. Verifikasi walkthrough kembali ke Step 1
8. Klik `[Next]`
9. Klik `[Next]`
10. Klik `[Done]`
11. Verifikasi `[Done]` menutup walkthrough
12. Muat ulang halaman (F5)
13. Verifikasi Table Tools tampil
14. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-GS-UCF-23: Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip

15. Ganti akun: logout, lalu login sebagai Total Control Client A (First Visit A)
16. Buka Global Settings > User > Custom Field
17. Verifikasi walkthrough muncul otomatis di Step 1
18. Klik `[Skip]`
19. Verifikasi `[Skip]` menutup walkthrough
20. Muat ulang halaman (F5)
21. Verifikasi Table Tools tampil
22. Verifikasi walkthrough tidak muncul setelah muat ulang

### TC-GS-UCF-24: Klik overlay gelap menutup walkthrough dan menyimpan flag seen

23. Ganti akun: logout, lalu login sebagai Total Control Client A (First Visit B)
24. Buka tab Custom Field (Global Settings > User > Custom Field)
25. Klik area overlay gelap di luar tooltip box
26. Verifikasi walkthrough tertutup
27. Muat ulang halaman (F5)
28. Verifikasi Table Tools tampil
29. Verifikasi walkthrough tidak muncul lagi setelah muat ulang

### TC-GS-UCF-401: Klik [Done] pada langkah terakhir walkthrough kunjungan pertama menyimpan flag seen

30. Ganti akun: logout, lalu login sebagai Total Control Client A (First Visit D)
31. Buka Global Settings > User > Custom Field
32. Verifikasi walkthrough muncul otomatis di Step 1 (`Step 1 of 3`)
33. Klik `[Next]` pada Step 1
34. Klik `[Next]` pada Step 2
35. Verifikasi pada Step 3 tombol `[Next]` berganti `[Done]`
36. Klik `[Done]` pada Step 3
37. Verifikasi `[Done]` menutup walkthrough
38. Muat ulang halaman (F5)
39. Verifikasi Table Tools tampil
40. Verifikasi walkthrough tidak muncul setelah muat ulang

### TC-GS-UCF-402: Esc pada walkthrough kunjungan pertama menutupnya dan menyimpan flag seen

41. Ganti akun: logout, lalu login sebagai Total Control Client A (First Visit E)
42. Buka Global Settings > User > Custom Field
43. Verifikasi walkthrough muncul otomatis di Step 1
44. Tekan Esc saat Step 1 tampil
45. Verifikasi Esc menutup walkthrough
46. Muat ulang halaman (F5)
47. Verifikasi Table Tools tampil
48. Verifikasi walkthrough tidak muncul setelah muat ulang

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 25, 23, 24, 401, 402. TC-GS-UCF-25 (akun Total Control, flag true) ditaruh pertama karena akun itu login di hook `before`; empat TC kunjungan pertama memakai akun First Visit masing-masing sehingga tiap blok berdiri sendiri dan tidak perlu mereset flag di tengah spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15, 23, 30, dan 41 (ganti akun), langkah 16, 24, 31, dan 42 (membuka tab Custom Field sebagai pemicu kunjungan pertama), langkah 12, 20, 27, 38, dan 46 (muat ulang halaman; langkah berikutnya adalah `Verifikasi` Table Tools tampil sebagai anchor absence setelah F5, bagian 8b butir 2), serta langkah 5, 8, 9, dan 10 pada TC-GS-UCF-25 (navigasi walkthrough).
- Spec 005 menguji konten step, navigasi keyboard, aktor Read Only, dan resize atau navigasi keluar pada tab yang sama; spec 006 dipisah karena tiap blok kunjungan pertama memakai akun First Visit sendiri dan flag seen sendiri.
- Spec melewati sekitar 35 langkah (48 langkah). Seluruhnya satu kelas (flag seen Guided Tooltip tab Custom Field); tiap blok TC memakai akun dan flag sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan langkah ganti akun eksplisit ada di awal tiap blok.
- Temuan untuk QA:
  - Post Condition TC-GS-UCF-23, 401, dan 402 ("Flag ... = true untuk akun First Visit ...") tidak punya langkah observasi di TC dan tidak punya Expected padanan; tidak diasersi di spec ini (S-01). Perilaku flag teramati lewat asersi "tidak muncul setelah muat ulang".
  - TC-GS-UCF-23, 24, 25, 401, dan 402 mensyaratkan flag seen belum ada atau sudah true tanpa menyebut cara menyetelnya; mekanismenya disediakan tim FE/BE.
  - Akun First Visit A, B, D, dan E tidak punya env var terdaftar di `.env.example`; nama `GS_FVA_TC_PASSWORD`, `GS_FVB_TC_PASSWORD`, `GS_FVD_TC_PASSWORD`, dan `GS_FVE_TC_PASSWORD` adalah usulan.
  - TC-GS-UCF-24 langkah 2 tidak menyebut titik klik pada overlay gelap; spec mengklik area overlay di luar spotlight dan tooltip box.
  - TC-GS-UCF-25 langkah 4 menulis "Klik [Next], [Next], [Done]" setelah `[Back]`; spec menjalankannya sebagai tiga klik berurutan dan mengasersi `[Done]` menutup walkthrough, sesuai Expected c.
