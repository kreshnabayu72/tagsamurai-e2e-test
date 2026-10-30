---
id: TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout
title: "Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Kegagalan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-85
  - TC-GS-UCF-86
  - TC-GS-UCF-131
  - TC-GS-UCF-132
  - TC-GS-UCF-339
coverage:
  web: automated
---

# Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Kegagalan

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata); dasar: pengecualian resilience `Mode: mock` di `docs/e2e-conventions.md` bagian 6 (spec hanya mengasersi perilaku FE atas respons mock). Endpoint yang dipanggil halaman pada kondisi tes, rujukan `API/openapi.yaml` dan `API/low-level-design.md` modul (angka = nomor baris berkas), dan respons yang dipaksa:
  - Daftar Custom Field, `POST /v2/iam/user-custom-fields/list` (openapi.yaml:13, low-level-design.md:15): memuat tiga baris Edit-target `Edit Meta Final {runId}-030` (Text), `Value Fail DD {runId}-030` (Dropdown `Aa`, `Bb`, `Cc`; nilai User Rahmat Hidayat = `Bb`), dan `Timeout Edit {runId}-030` (Text). Isi list tidak diasersi setelah create atau edit.
  - Request create Custom Field, `POST /v2/iam/user-custom-fields` (openapi.yaml:326, low-level-design.md:362; path sama dengan TC-GS-UCF-304): respons 500 (TC-GS-UCF-85, lalu respons sukses pada pengulangan Submit), tanpa respons sampai timeout (TC-GS-UCF-86).
  - Request edit Custom Field, `PATCH /v2/iam/user-custom-fields/{id}` (openapi.yaml:440, low-level-design.md:550; path sama dengan TC-GS-UCF-305): respons 500 (TC-GS-UCF-131 dan 132; TC-GS-UCF-131 lalu respons sukses pada pengulangan Save), tanpa respons sampai timeout (TC-GS-UCF-339).
  - Cek ketersediaan nama, `POST /v2/iam/user-custom-fields/check-availability` (openapi.yaml:292, low-level-design.md:314): respons normal (nama tersedia).
  - Endpoint modul lain pada openapi (`GET /v2/iam/user-custom-fields/dropdown` openapi.yaml:199 dan low-level-design.md:221, `GET /v2/iam/user-custom-fields/used` openapi.yaml:243 dan low-level-design.md:274, `POST /v2/iam/user-custom-fields/options` openapi.yaml:89 dan low-level-design.md:93): respons normal bila halaman memanggilnya pada kondisi tes; apakah halaman memanggilnya dikonfirmasi tim FE.
  - Detail User (section Custom Fields): respons normal, `Bb` tetap tampil pada Detail User Rahmat Hidayat; endpoint-nya bukan bagian openapi modul ini (disediakan tim FE).
  - SSE Custom Field: tidak ada di `openapi.yaml` maupun `low-level-design.md`; PRD (`custom-field-user.md:934`) menyatakan modul ini tidak mengirim event SSE, sehingga tidak ada event selama spec ini (stream, bila halaman berlangganan, disediakan tim FE).
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar `[+ Custom Field]` dan row action Edit tampil, flag Guided Tooltip, Detail User) disediakan tim FE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`; pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis (hanya sebagai isi respons mock, tidak ada data yang dibuat di backend): `Fail One {runId}-030`, `Slow Net {runId}-030`, serta tiga baris Edit-target di atas. Fixture baru `Fixture.customFieldUser.resilienceWrite030`. Data Pre-setup tidak dipakai.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini; tutup form yang masih terbuka.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500, menahan respons sampai timeout, dan mengganti respons di tengah spec; membaca toast dan men-dismiss toast.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-85: Create gagal 5xx mempertahankan form dan input

1. Pasang intercept pada request create Custom Field: respons 500
2. Klik `[+ Custom Field]`
3. Isi Field Name `Fail One {runId}-030`, Data Type `Text`
4. Klik `[Submit]`
5. Verifikasi toast error: "Error, failed to create custom field."
6. Verifikasi popup tetap terbuka
7. Verifikasi input Field Name `Fail One {runId}-030` dan Data Type `Text` dipertahankan
8. Verifikasi `[Submit]` enabled kembali
9. Dismiss toast error
10. Lepas intercept 500 dan pasang mock respons create sukses
11. Klik `[Submit]`
12. Verifikasi toast sukses: "Success, custom field has been created."
13. Lepas mock respons create sukses

### TC-GS-UCF-86: Create timeout mempertahankan form dan menawarkan coba ulang

14. Pasang intercept pada request create Custom Field: tanpa respons sampai timeout
15. Klik `[+ Custom Field]`
16. Isi Field Name `Slow Net {runId}-030`, Data Type `Text`
17. Klik `[Submit]`
18. Verifikasi toast error `Connection problem. Please try again.`
19. Verifikasi toast error memuat tombol `[Try Again]`
20. Verifikasi popup tetap terbuka
21. Verifikasi input Field Name `Slow Net {runId}-030` dan Data Type `Text` dipertahankan
22. Verifikasi `[Submit]` enabled kembali
23. Dismiss toast error
24. Lepas intercept timeout
25. Klik `[✕]`
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

### TC-GS-UCF-131: Save gagal 5xx mempertahankan popup dan input

28. Pasang intercept pada request edit Custom Field: respons 500
29. Klik `⋯` pada baris `Edit Meta Final {runId}-030`, pilih `Edit`
30. Ubah Placeholder menjadi `Fail`
31. Klik `[Save]`
32. Verifikasi toast error: "Error, failed to update custom field."
33. Verifikasi popup tetap terbuka
34. Verifikasi Placeholder `Fail` dipertahankan
35. Verifikasi `[Save]` enabled
36. Dismiss toast error
37. Lepas intercept 500 dan pasang mock respons edit sukses
38. Klik `[Save]`
39. Verifikasi toast sukses: "Success, custom field has been updated."
40. Lepas mock respons edit sukses

### TC-GS-UCF-132: Save gagal 5xx setelah rename dan remove value mempertahankan perubahan form dan tidak mengubah nilai User

41. Pasang intercept pada request edit Custom Field: respons 500
42. Klik `⋯` pada baris `Value Fail DD {runId}-030`, pilih `Edit`
43. Ubah badge `Aa` menjadi `Aaa`, tekan Enter
44. Klik `×` pada `Bb`, klik `[Remove]`
45. Klik `[Save]`
46. Verifikasi toast error: "Error, failed to update custom field."
47. Verifikasi popup tetap terbuka
48. Verifikasi badge `Aaa` dan `Cc` dipertahankan (`Bb` sudah dihapus dari form)
49. Verifikasi `[Save]` enabled
50. Dismiss toast error
51. Lepas intercept 500
52. Klik `[✕]`
53. Verifikasi dialog `Unsaved Changes` tampil
54. Klik `[Leave]`
55. Verifikasi Value Setting baris `Value Fail DD {runId}-030` tetap `Aa`, `Bb`, `Cc`
56. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
57. Verifikasi Detail User Rahmat Hidayat tetap menampilkan `Bb` pada `Value Fail DD {runId}-030`
58. Buka Global Settings > User > Custom Field

### TC-GS-UCF-339: Edit timeout mempertahankan form dan menawarkan coba ulang

59. Pasang intercept pada request edit Custom Field: tanpa respons sampai timeout
60. Klik `⋯` pada baris `Timeout Edit {runId}-030`, pilih `Edit`
61. Ubah Placeholder menjadi `Slow`
62. Klik `[Save]`
63. Verifikasi toast error `Connection problem. Please try again.`
64. Verifikasi toast error memuat tombol `[Try Again]`
65. Verifikasi popup tetap terbuka
66. Verifikasi Placeholder `Slow` dipertahankan
67. Verifikasi `[Save]` enabled kembali
68. Dismiss toast error
69. Lepas intercept timeout
70. Klik `[✕]`
71. Verifikasi dialog `Unsaved Changes` tampil
72. Klik `[Leave]`

## Notes

- Mode: mock. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: fault injection (bagian 3 prinsip 13b), satu spec untuk Create dan Edit.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 72 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas harness (fault injection pada tulis form), satu akun, dan tiap blok berdiri sendiri dengan respons mock sendiri; jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Langkah penghubung (aksi tanpa `Verifikasi`): memasang dan melepas intercept dan mock respons (S-09, intercept dilepas segera setelah pemicu), men-dismiss toast error sebelum asersi toast berikutnya, membuka Detail User, kembali ke tab Custom Field, serta menutup form dirty lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` (S-08).
- Pada TC-GS-UCF-85 dan 131 pengulangan Submit atau Save memakai mock respons sukses; keadaan popup sesudah toast sukses tidak diasersi karena tidak ada di Expected TC.
- Pembagian TC lintas spec: kegagalan 5xx dan timeout pada Delete dan Toggle ada di spec 049; kegagalan baca ada di spec 011; kegagalan download ada di spec 060.
- Temuan untuk QA:
  - Keputusan user: resilience yang memaksa 5xx atau timeout ditulis `Mode: mock` (pengecualian resilience di `docs/e2e-conventions.md` bagian 6). Bagian 6 itu menetapkan asersi yang membutuhkan state server nyata dipecah ke TC FE+BE terpisah; pemecahan TC belum dikerjakan. TC-GS-UCF-132 mengasersi state backend ("definisi field tetap `Aa`, `Bb`, `Cc`" langkah 55 dan "Detail User Rahmat Hidayat tetap `Bb`" langkah 56 sampai 57); pada mode mock langkah itu hanya membuktikan bahwa FE tidak mengubah tampilan setelah error, bukan integritas data server. Asersi tetap ditulis sesuai TC sampai QA memecah TC-GS-UCF-132 ke TC FE+BE yang di-intercept di atas backend nyata; setelah itu langkah 55 sampai 58 pindah ke spec FE+BE.
  - TC-GS-UCF-85 dan 86 memakai nama `Fail One` dan `Slow Net`; spec memakai versi bersuffix `{runId}-030` (S-12). TC-GS-UCF-86 tidak menyebut keadaan popup yang ditutup sesudah timeout; spec menutupnya lewat `✕` dan `[Leave]` sebagai penghubung.
  - TC-GS-UCF-85, 86, 131, 132, 339: tidak ada Post Condition. TC tidak menyebut path endpoint; spec mengambil path dan rujukan baris dari `openapi.yaml` dan `low-level-design.md` modul (S-13), kecuali Detail User dan SSE yang tidak ada di sumber modul.
  - TC-GS-UCF-86 dan 339 menulis toast `Connection problem. Please try again.` dengan tombol `[Try Again]`; TC tidak menyebut apakah klik `[Try Again]` menjadi bagian uji, sehingga tombol hanya diasersi tampil.
