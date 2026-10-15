---
id: TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh
title: "Popup Concurrent Session Limit Reached saat Seat Penuh"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-96
  - TC-AUTH-SES-97
  - TC-AUTH-SES-98
  - TC-AUTH-SES-99
  - TC-AUTH-SES-100
coverage:
  web: automated
---

# Popup Concurrent Session Limit Reached saat Seat Penuh

## Prerequisites

- Mode: FE+BE.
- Kelas harness e (volume data khusus: kuota seat). Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota Fixed Asset 2; tidak ada sesi-produk Fixed Asset Active selain dua seed di bawah (spec lain melepas seat miliknya di hook `after`).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE milik Client Q2 dengan App Access Fixed Asset dan Supply Asset (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Seed seat: `Gunawan Prakoso` (`gunawanprakoso+{runId}-030@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-030@qwertysystem.net`), masing-masing dengan sesi platform web Active dan satu sesi-produk Fixed Asset Active sehingga seat terpakai 2 dari kuota 2 (seat penuh) selama seluruh spec
  - TC-AUTH-SES-96: `Agus Ramadhan` (`agusramadhan+{runId}-030@qwertysystem.net`)
  - TC-AUTH-SES-97: `Rina Wulandari` (`rinawulandari+{runId}-030@qwertysystem.net`)
  - TC-AUTH-SES-98: `Hendra Hidayat` (`hendrahidayat+{runId}-030@qwertysystem.net`)
  - TC-AUTH-SES-99: `Maya Utami` (`mayautami+{runId}-030@qwertysystem.net`)
  - TC-AUTH-SES-100: `Fajar Puspita` (`fajarpuspita+{runId}-030@qwertysystem.net`)
- Sesi platform web Active untuk kelima user TC di Browser A (Chrome on Windows, konteks browser terpisah per TC) dibuat di hook `before` lewat login API pada konteks Browser A masing-masing; tidak ada sesi-produk Fixed Asset milik kelima user itu.
- Konteks browser (hook `before`): Browser Admin login oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26); Browser License login oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License di Client Q2, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`).
- Hook `after`: akhiri semua sesi dan sesi-produk seed (termasuk dua seed seat), tutup semua konteks browser, lalu hapus ketujuh user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- State global yang diubah: seat Fixed Asset Client Q2 (diisi penuh oleh seed). Pemulihan di hook `after`; suite berjalan serial.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: banyak konteks browser bersamaan; navigasi langsung ke URL dashboard Fixed Asset (TC-AUTH-SES-100); penekanan Escape dan klik area backdrop popup; pembacaan status sesi platform dan status sesi-produk dari BE oleh akun aktor.
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor Manage Global License pada Browser License; akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-96: Buka produk saat seat penuh memunculkan Popup Concurrent session limit reached dan tidak membuat sesi-produk

1. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil dengan hitungan seat aktif 2 dari kuota 2
2. Di Browser A buka Portal — Product Hub sebagai `agusramadhan+{runId}-030@qwertysystem.net` → halaman Portal — Product Hub tampil
3. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Agus Ramadhan`, catat baseline: jumlah entri Note `Concurrent limit reached` dengan email `agusramadhan+{runId}-030@qwertysystem.net` di masing-masing log
4. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup muncul
5. Verifikasi Popup "Concurrent session limit reached" tampil dengan Body "You've reached the concurrent session limit for this product. Try again later once a session becomes available."
6. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
7. Verifikasi Sesi-produk Fixed Asset `Agus Ramadhan` tidak dibuat (baris `Agus Ramadhan` tidak ada pada daftar)
8. Verifikasi Hitungan seat aktif tetap 2
9. Verifikasi Sesi platform `Agus Ramadhan` tetap Active
10. Verifikasi Browser A tetap di Portal — Product Hub
11. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Agus Ramadhan`, cari entri berdasarkan Note `Concurrent limit reached` dan email `agusramadhan+{runId}-030@qwertysystem.net` → halaman log tampil
12. Verifikasi Jumlah entri `Concurrent limit reached` untuk `Agus Ramadhan` bertambah 1 terhadap baseline di `Activity Log > Session` milik Fixed Asset
13. Verifikasi Jumlah entri `Concurrent limit reached (Fixed Asset)` untuk `Agus Ramadhan` bertambah 1 terhadap baseline di `Global Settings > User > Detail > User Log`

### TC-AUTH-SES-97: OK pada Popup Concurrent session limit reached menutup popup dan tetap di Portal

14. Tutup konteks Browser A sebelumnya dan buka konteks Browser A baru untuk `Rina Wulandari` dengan sesi platform web Active
15. Di Browser A buka Portal — Product Hub sebagai `rinawulandari+{runId}-030@qwertysystem.net` → halaman Portal — Product Hub tampil
16. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup "Concurrent session limit reached" muncul
17. Klik [OK] pada popup
18. Verifikasi Popup tertutup
19. Verifikasi Browser A tetap di Portal — Product Hub
20. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
21. Verifikasi Tidak ada sesi-produk baru (baris `Rina Wulandari` tidak ada pada daftar dan hitungan seat aktif tetap 2)

### TC-AUTH-SES-98: Escape pada Popup Concurrent session limit reached menutup popup dengan efek OK

22. Tutup konteks Browser A sebelumnya dan buka konteks Browser A baru untuk `Hendra Hidayat` dengan sesi platform web Active
23. Di Browser A buka Portal — Product Hub sebagai `hendrahidayat+{runId}-030@qwertysystem.net` → halaman Portal — Product Hub tampil
24. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup "Concurrent session limit reached" muncul
25. Tekan tombol Escape
26. Verifikasi Popup tertutup
27. Verifikasi Browser A tetap di Portal — Product Hub
28. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
29. Verifikasi Tidak ada sesi-produk baru (baris `Hendra Hidayat` tidak ada pada daftar dan hitungan seat aktif tetap 2)

### TC-AUTH-SES-99: Klik backdrop pada Popup Concurrent session limit reached menutup popup dengan efek OK

30. Tutup konteks Browser A sebelumnya dan buka konteks Browser A baru untuk `Maya Utami` dengan sesi platform web Active
31. Di Browser A buka Portal — Product Hub sebagai `mayautami+{runId}-030@qwertysystem.net` → halaman Portal — Product Hub tampil
32. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup "Concurrent session limit reached" muncul
33. Klik area gelap di luar popup
34. Verifikasi Popup tertutup
35. Verifikasi Browser A tetap di Portal — Product Hub
36. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
37. Verifikasi Tidak ada sesi-produk baru (baris `Maya Utami` tidak ada pada daftar dan hitungan seat aktif tetap 2)

### TC-AUTH-SES-100: Deep-link ke URL produk saat seat penuh: OK mengarahkan ke Portal dan halaman produk tidak dimuat

38. Tutup konteks Browser A sebelumnya dan buka konteks Browser A baru untuk `Fajar Puspita` dengan sesi platform web Active
39. Di Browser A buka Portal — Product Hub sebagai `fajarpuspita+{runId}-030@qwertysystem.net` → halaman Portal — Product Hub tampil
40. Di Browser A buka langsung URL dashboard Fixed Asset (tanpa lewat Portal) → Popup muncul
41. Verifikasi Popup "Concurrent session limit reached" tampil
42. Verifikasi Halaman Fixed Asset di belakang popup tidak dimuat selama popup tampil
43. Klik [OK] pada popup
44. Verifikasi Browser A diarahkan ke Portal — Product Hub

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness e (kuota seat, seed seat penuh).
- Urutan mengikuti TC sumber (96, 97, 98, 99, 100). TC-AUTH-SES-96 pertama karena memuat asersi popup dan pencatatan; TC-AUTH-SES-97 sampai 99 berdependensi pada TC-AUTH-SES-96 dan menyalin langkah TC-AUTH-SES-96 (buka Portal lalu klik card Fixed Asset hingga popup muncul; langkah 15 dan 16, 23 dan 24, 31 dan 32) di awal tiap TC (S-04). Tiap TC memakai user sendiri; seat penuh dipertahankan oleh dua seed milik spec sehingga TC tidak saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka Portal sebagai user TC; mencatat baseline entri log (langkah 3); menutup konteks Browser A sebelumnya dan membuka konteks baru saat berganti user antar-TC; muat ulang daftar Concurrent User; membuka halaman log. Asersi tambahan di luar Expected: pembacaan daftar Concurrent User pada TC-AUTH-SES-96 sampai 99 untuk membuktikan "sesi-produk tidak dibuat" dan "seat aktif tetap 2".
- Ukuran spec 44 langkah: lima TC berbagi satu kondisi seat penuh (dua seed milik spec) dan tiap TC memakai user serta konteks Browser A sendiri, sehingga TC sesudahnya tetap bermakna bila TC sebelumnya gagal; memecahnya berarti mengulang seeding seat penuh per spec.
- Asersi pencatatan `Concurrent limit reached` (langkah 11 sampai 13; baseline langkah 3 di Activity Log Session Fixed Asset dan User Log) mengikuti rujukan TC-AUTH-SES-96 ke TC-AUTH-SES-204 untuk lokasi log; log tidak diasersi pada TC-AUTH-SES-97 sampai 100. Pencatatan tidak muncul di GS Session ditangani spec absence `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent` (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-96 sampai 100 tidak menyebut cara mengamati "seat aktif tetap 2" di UI; spec membaca daftar dan hitungan seat di License > Concurrent User sesuai pola TC-AUTH-SES-95. (2) TC-AUTH-SES-97 sampai 99 menyatakan popup "sedang tampil" sebagai precondition tanpa menyebut cara memunculkannya; spec menyalin langkah dari TC-AUTH-SES-96. (3) TC-AUTH-SES-100 tidak menyebut cara membuktikan "halaman Fixed Asset tidak dimuat selama popup tampil"; spec mengasersi lewat kondisi dashboard Fixed Asset tidak tampil di belakang popup. (4) Akun #2 `manageGlobalLicenseFixedAsset` pada Tabel Data Uji Pre-setup tidak menyebut Client cakupannya; spec mengasumsikan scope Client Q2.
