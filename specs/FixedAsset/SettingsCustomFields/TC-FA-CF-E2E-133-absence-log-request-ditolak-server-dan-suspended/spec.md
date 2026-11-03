---
id: TC-FA-CF-E2E-133-absence-log-request-ditolak-server-dan-suspended
title: "Absence Log: Request Langsung Ditolak dan Aksi Saat Client Suspended"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-555
  - TC-FA-CF-584
  - TC-FA-CF-659
coverage:
  web: automated
---

# Absence Log: Request Langsung Ditolak dan Aksi Saat Client Suspended

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Read Only Company Alpha `readOnly_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #3). Login di hook `before` spec ini dengan `Spectra.env.FA_RO_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 10): Total Control Company Alpha, pengguna Sarah Johnson (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`. Akun ketiga (langkah 17): Total Control Client Suspended (Pre-setup #22) dengan `Spectra.env.FA_TC_SUSPENDED_PASSWORD` (email tidak tertulis di Pre-setup TC; disediakan tim FE). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Client Suspended (Pre-setup #22): entitas Suspended dengan field baseline #12 (`Depreciated Ratio` Inactive).
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan token `Read Only` (login API password) dan status entitas Suspended lewat seed; asersi request langsung hanya status respons dan state data (8b butir 1).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- State global: tidak ada yang diubah oleh spec (status Suspended Client Suspended adalah baseline Company itu).
- Data Dinamis: nama payload `Direct RO {runId}-133` dan `Susp Create {runId}-133` (tidak pernah tersimpan). Seed reset Company memulihkan baseline di hook `before` dan `after`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-555: Request Create langsung oleh Read Only ditolak 403 tanpa mengubah data

1. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log Company Alpha sebagai baseline (kemampuan baca disediakan tim FE/BE)
2. Kirim request Create custom field langsung ke server dengan token `Read Only` (payload valid: Field Name `Direct RO {runId}-133`, Data Type `Text`, Scope `General`)
3. Verifikasi server merespons 403 Forbidden
4. Muat ulang (F5) halaman Settings > Custom Fields sebagai `Read Only` (Pre-setup #3)
5. Verifikasi Breadcrumb `Settings > Custom Fields` dan baris `Asset Serial Tag` tampil
6. Verifikasi elemen tulis `[+ Custom Field]` tetap Hidden
7. Ketik Search `Direct RO {runId}-133`, tekan Enter
8. Verifikasi empty state `No results found` tampil (tidak ada field baru)
9. Klik `(←)` pada kotak Search
10. Ganti akun: logout, lalu login sebagai Total Control Company Alpha (Pre-setup #1)
11. Buka Modal Changelog tab General dan hitung ulang jumlah entri
12. Verifikasi jumlah entri Changelog tab General sama dengan baseline
13. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
14. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
15. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
16. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-584: Create saat entitas Suspended ditolak 403 dengan toast entitas baku

17. Ganti akun: logout, lalu login sebagai Total Control Client Suspended (Pre-setup #22)
18. Catat jumlah entri Changelog tab General, System Log `Total Control` aktor, dan Activity Log Client Suspended sebagai baseline
19. Klik `[+ Custom Field]`, isi Field Name `Susp Create {runId}-133` dan Data Type `Text`
20. Klik `[Submit]`
21. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
22. Tutup toast error
23. Verifikasi halaman tetap di Settings > Custom Fields tanpa redirect (Breadcrumb `Settings > Custom Fields` tampil)
24. Verifikasi modal Create tertutup otomatis
25. Verifikasi tabel di-refresh dan baris `Asset Serial Tag` tampil
26. Ketik Search `Susp Create {runId}-133`, tekan Enter
27. Verifikasi empty state `No results found` tampil (tidak ada field baru)
28. Klik `(←)` pada kotak Search
29. Buka Modal Changelog tab General dan hitung ulang jumlah entri
30. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri log dari Submit ini)
31. Buka System Log aktor Client Suspended dan hitung ulang jumlah entri
32. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak ada entri log dari Submit ini)
33. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
34. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri log dari Submit ini)

### TC-FA-CF-659: Activate saat entitas Suspended ditolak

35. Catat jumlah entri Changelog tab General, System Log aktor, dan Activity Log Client Suspended sebagai baseline, lalu kembali ke Settings > Custom Fields (tab General)
36. Geser switch `Depreciated Ratio` ke ON
37. Klik `[Activate]` pada dialog
38. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
39. Tutup toast error
40. Verifikasi dialog Activate tertutup
41. Verifikasi tabel di-refresh dan baris `Asset Serial Tag` tampil
42. Verifikasi switch `Depreciated Ratio` kembali ke posisi OFF
43. Muat ulang (F5) halaman Settings > Custom Fields
44. Verifikasi baris `Asset Serial Tag` tampil dan switch `Depreciated Ratio` tetap pada posisi OFF (status tidak berubah)
45. Buka Modal Changelog tab General dan hitung ulang jumlah entri
46. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri log)
47. Buka System Log aktor Client Suspended dan hitung ulang jumlah entri
48. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak ada entri log)
49. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
50. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri log)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 50 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log; 18 langkah, nomor 11 sampai 16, 29 sampai 34, 45 sampai 50) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 32 langkah. Spec dipertahankan karena semua blok satu kelas harness (asersi absence log); tiap TC punya user dan baseline sendiri (P-5 butir a) dan berdiri sendiri.
- P-5 (a): spec absence kelas g; pemicu kelas a (request Create langsung dengan token `Read Only`) dan kelas h (Client Suspended) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya user dan baseline sendiri (S-12). TC-FA-CF-665 (Grace Period) ada di spec 179.
- Anchor positif (8b butir 2): respons 403, toast entitas baku, serta jumlah entri awal yang dicatat pada baseline tiap TC; asersi "tidak ada entri" ditulis sebagai kesamaan jumlah entri dengan baseline. Absence field baru memakai empty state `No results found` sebagai anchor.
- Urutan TC di spec: 555 (Company Alpha), 584 dan 659 (Client Suspended, tanpa ganti akun di antaranya). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 17 (ganti akun eksplisit), baseline, langkah 22 dan 39 (menutup toast error sebelum aksi atau asersi toast berikutnya, R-12), dan langkah buka surface serta hitung ulang jumlah entri.
- Request langsung (langkah 2) tidak melewati browser: yang diasersi hanya status respons dan state data; perilaku FE untuk Read Only diasersi pada halaman yang dimuat ulang sesuai TC (langkah 4 sampai 6).
- K-1: TC-FA-CF-555 dan TC-FA-CF-584 kelas a dengan Expected respons API tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Temuan untuk QA:
  - TC-FA-CF-555 Expected c tidak merinci elemen tulis yang Hidden; spec mengasersi `[+ Custom Field]` saja.
  - TC-FA-CF-555 tidak menyebut aktor pembaca log; spec memakai Total Control Company Alpha dan membaca jumlah entri lewat kemampuan baca FE/BE.
  - TC-FA-CF-584 Expected a mencantumkan "tabel di-refresh" tanpa cara mengamatinya; spec mengasersi tabel termuat dengan baris `Asset Serial Tag` tampil.
  - Email akun Total Control Client Suspended tidak tertulis di Pre-setup TC; env var `FA_TC_SUSPENDED_PASSWORD` disediakan tim FE.
