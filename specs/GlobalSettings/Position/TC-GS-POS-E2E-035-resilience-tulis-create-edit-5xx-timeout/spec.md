---
id: TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout
title: "Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-67
  - TC-GS-POS-68
  - TC-GS-POS-106
  - TC-GS-POS-107
  - TC-GS-POS-108
coverage:
  web: automated
---

# Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Respons yang dipaksa:
  - Daftar Position (`POST /v2/iam/positions/list`, LLD:9, openapi:11): memuat 1 baris `Payroll Specialist {runId}-035` (baris target Edit). Isi list tidak diasersi setelah create atau edit.
  - Request create Position (`POST /v2/iam/positions`, LLD:164, openapi:265): respons 500 (langkah 1), respons sukses (langkah 12), lalu tanpa respons sampai timeout (langkah 17).
  - Request edit Position (`PATCH /v2/iam/positions/{position_id}`, LLD:318, openapi:440): respons 500 (langkah 31), tanpa respons sampai timeout (langkah 40), perubahan tersimpan di data mock tetapi respons timeout (langkah 46), lalu respons sukses no-op (langkah 49; PRD §9.6 dan EC-07: Name setelah trim identik nilai tersimpan menghasilkan no-op success).
  - Cek ketersediaan nama (`POST /v2/iam/positions/check-availability`, LLD:127, openapi:189): dipanggil form Create dan Edit saat nama diketik; respons normal (nama tersedia), tanpa asersi.
  - SSE `position.created`, `position.updated`, dan `position.deleted` (LLD:182, :337, :260): halaman berlangganan; stream disediakan tim FE dan tidak ada event yang dikirim selama spec ini.
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar `[+ Position]` dan row action Edit tampil) disediakan tim FE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`; pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis (hanya sebagai isi respons mock, tidak ada data yang dibuat di backend): `Internal Auditor {runId}-035`, `Internal Auditor II {runId}-035`, `Payroll Specialist {runId}-035` yang diubah menjadi `Payroll Manager {runId}-035`. Fixture baru `Fixture.position.resilienceWrite035`. Data Pre-setup tidak dipakai.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini; tutup form yang masih terbuka.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500, menahan respons sampai timeout, dan mengganti respons mock di tengah spec; membaca toast beserta ketahanannya (toast error tidak hilang otomatis; toast sukses hilang otomatis setelah 4 detik, `foundation/functions/toast-copy.md`) dan men-dismiss toast.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-POS-67: Create, kegagalan server 5xx mempertahankan form

1. Pasang intercept pada request create Position: respons 500
2. Klik `[+ Position]`
3. Verifikasi User > Position > Popup Create Position terbuka
4. Ketik `Internal Auditor {runId}-035` pada Position Name
5. Klik `[Submit]`
6. Verifikasi toast error "Error, failed to create position." tampil
7. Verifikasi toast error tetap tampil setelah jeda melebihi 4 detik (durasi hilang otomatis toast sukses), tidak hilang otomatis
8. Verifikasi popup Create Position tetap terbuka
9. Verifikasi nilai `Internal Auditor {runId}-035` dipertahankan pada Position Name
10. Verifikasi `[Submit]` enabled
11. Dismiss toast error
12. Lepas intercept 500 dan pasang mock respons create sukses
13. Klik `[Submit]`
14. Verifikasi toast sukses "Success, position has been created."
15. Verifikasi popup Create Position tertutup
16. Lepas mock respons create sukses

### TC-GS-POS-68: Create, timeout jaringan saat Submit

17. Pasang intercept pada request create Position: tanpa respons sampai timeout
18. Klik `[+ Position]`
19. Verifikasi User > Position > Popup Create Position terbuka
20. Ketik `Internal Auditor II {runId}-035` pada Position Name
21. Klik `[Submit]`
22. Verifikasi toast error "Connection problem. Please try again." tampil
23. Dismiss toast error "Connection problem. Please try again."
24. Verifikasi popup Create Position tetap terbuka
25. Verifikasi nilai `Internal Auditor II {runId}-035` dipertahankan pada Position Name
26. Verifikasi `[Submit]` enabled
27. Lepas intercept timeout
28. Klik `✕` di header untuk menutup popup
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

### TC-GS-POS-106: Edit, kegagalan server 5xx mempertahankan form

31. Pasang intercept pada request edit Position: respons 500
32. Klik `⋯` pada baris `Payroll Specialist {runId}-035`, pilih `Edit`
33. Verifikasi User > Position > Popup Edit Position terbuka
34. Ganti nilai Position Name menjadi `Payroll Manager {runId}-035`
35. Klik `[Save]`
36. Verifikasi toast error "Error, failed to update position." tampil
37. Verifikasi popup Edit Position tetap terbuka
38. Verifikasi nilai `Payroll Manager {runId}-035` dipertahankan pada Position Name
39. Verifikasi `[Save]` enabled

### TC-GS-POS-107: Edit, timeout jaringan saat Save

40. Dismiss toast error "Error, failed to update position.", lalu ganti intercept pada request edit Position: tanpa respons sampai timeout
41. Klik `[Save]`
42. Verifikasi toast error "Connection problem. Please try again." tampil
43. Dismiss toast error "Connection problem. Please try again."
44. Verifikasi popup Edit Position tetap terbuka
45. Verifikasi input Position Name tetap `Payroll Manager {runId}-035`

### TC-GS-POS-108: Edit, retry setelah timeout yang ternyata sudah tersimpan diperlakukan No-Op

46. Ganti intercept pada request edit Position: perubahan tersimpan di data mock (record menjadi `Payroll Manager {runId}-035`) tetapi respons ke browser timeout
47. Klik `[Save]`
48. Verifikasi toast error "Connection problem. Please try again." tampil
49. Ganti intercept pada request edit Position: respons sukses no-op
50. Klik `[Save]` lagi
51. Verifikasi toast netral "No changes to save." tampil
52. Verifikasi popup Edit Position tertutup
53. Lepas intercept pada request edit Position

## Notes

- Mode: mock. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Tidak ada asersi yang membaca ulang isi respons mock list karena Expected TC tidak memintanya.
- Urutan TC dipertahankan (67, 68, 106, 107, 108). Pembukaan form: Create dibuka dua kali (langkah 2 dan 18) dan ditutup dua kali (langkah 15 lewat submit sukses, langkah 28 sampai 30 lewat `✕` dan `[Leave]`). Popup Edit dibuka sekali (langkah 32) dan dipakai bersama TC-GS-POS-106, 107, dan 108 karena setelah tiap kegagalan popup tetap terbuka dengan nilai yang sama seperti hasil membuka ulang dan mengganti nilai; popup tertutup di langkah 52 oleh retry No-Op.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 11, 12, 16, 17, 23, 27, 31, 40, 43, 46, 49, 53 (dismiss toast, pemasangan, penggantian, dan pelepasan intercept; langkah 23 dan 43 men-dismiss toast `Connection problem` supaya toast berikutnya yang sama tidak lulus karena toast lama), langkah 28 sampai 30 (penutupan form dirty deterministik sesuai S-08; dialog `Unsaved Changes` diasersi oleh langkah 29).
- Verifikasi langkah 15 (popup Create tertutup setelah submit sukses tanpa centang `Stay on this form after submitting`) tidak ada di Expected TC-GS-POS-67; ditambahkan sebagai penanda state sebelum langkah 18 yang membuka popup Create lagi (PRD FI-11).
- Retry TC-GS-POS-67 dan langkah 50 TC-GS-POS-108 diasersi dari toast dan tampilan; keadaan di server tidak dibaca.
- Spec melewati sekitar 35 langkah (53 langkah). Seluruhnya satu kelas (fault injection pada aksi tulis Create dan Edit, `Mode: mock`), satu akun, tanpa data nyata. Blok Create (langkah 1 sampai 30) dan blok Edit (langkah 31 sampai 53) berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lainnya. Di dalam blok Edit, TC-GS-POS-107 dan 108 memakai popup yang dibuka TC-GS-POS-106.
- Temuan untuk QA:
  - TC-GS-POS-108 berstatus Manual Only di TC tetapi tetap ditulis (konvensi bagian 2). Pada mode mock, "tersimpan di server tetapi respons timeout" ditiru dengan mengubah data mock; perilaku sebenarnya di server tidak teruji.
  - TC-GS-POS-67 dan 68 menulis `Internal Auditor` dan `Internal Auditor II` tanpa suffix; spec menambah suffix `{runId}-035` pada nama literal.
  - TC-GS-POS-106 dan 107 menyebut "Record `Payroll Specialist` ada" dengan dependensi TC-GS-POS-53; pada mode mock record cukup diberikan oleh respons mock list.
  - TC-GS-POS-107 tidak menyebut apakah popup dibuka ulang antar-TC; spec memakai popup yang sama (lihat butir urutan di atas).
  - Post Condition tanpa langkah observasi di TC tidak diasersi, dan state backend nyata tidak teruji pada mode mock: TC-GS-POS-67 ("tidak ada record dari percobaan gagal"), TC-GS-POS-106 ("Record tetap `Payroll Specialist`"), TC-GS-POS-108 (Changelog mencatat tepat 1 entri Edit).
