---
id: TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log
title: "Struktur, Kolom, dan Format Surface Log Sesi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-213
  - TC-AUTH-SES-214
  - TC-AUTH-SES-215
  - TC-AUTH-SES-249
  - TC-AUTH-SES-287
  - TC-AUTH-SES-288
  - TC-AUTH-SES-289
coverage:
  web: automated
---

# Struktur, Kolom, dan Format Surface Log Sesi

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; user dan seat milik Client Q2 untuk TC-AUTH-SES-215 oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)): tujuh user profil BASE (Tabel Data Uji Pre-setup #5 dan #12: Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Sesi dan entri log seed dibuat BE lewat aksi nyata (login, buka produk, logout) dari Browser A (Chrome on Windows) kecuali dinyatakan lain:
  - TC-AUTH-SES-213: `Nur Nugroho` (`nurnugroho+{runId}-061@qwertysystem.net`), Client Alpha Logistik; sesi sudah menghasilkan entri `Session started` dan `Logged out`
  - TC-AUTH-SES-214: `Agus Maulana` (`agusmaulana+{runId}-061@qwertysystem.net`), Client Alpha Logistik; sesi sudah membuka Fixed Asset dan Global Settings
  - TC-AUTH-SES-249: `Lestari Wibowo` (`lestariwibowo+{runId}-061@qwertysystem.net`), Client Alpha Logistik; sesi dibuat tanpa info device dan tanpa alamat IP terbaca (di-seed BE; mekanisme disediakan tim BE)
  - TC-AUTH-SES-288: `Yoga Maulana` (`yogamaulana+{runId}-061@qwertysystem.net`), Client Alpha Logistik tanpa Employee ID, Position, dan Division; sesi web Active di Browser A (Chrome on Windows)
  - TC-AUTH-SES-215: `Rina Wijaya` (`rinawijaya+{runId}-061@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: kuota Fixed Asset 2) dengan App Access Fixed Asset dan Supply Asset; dua user seed pemegang seat Client Q2 bersuffix milik spec ini, `Gunawan Prakoso` (`gunawanprakoso+{runId}-061@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-061@qwertysystem.net`), pola Tabel Data Uji Pre-setup #7. Urutan seed berikut dijalankan berurutan supaya `Rina Wijaya` punya riwayat sesi-produk sekaligus terblok concurrent (seat tidak penuh saat ia membuka produk, dan penuh saat ia diblok):
    1. `Rina Wijaya` login di Browser A, lalu dari Portal — Product Hub membuka Global Settings dan Fixed Asset (event `Session started` Global Settings dan `Session started` Fixed Asset)
    2. Sesi-produk Global Settings dan Fixed Asset milik `Rina Wijaya` diakhiri lewat API (disediakan tim BE; event `Session ended` kedua produk); sesi platform `Rina Wijaya` tetap Active dan seat Fixed Asset Client Q2 kembali kosong
    3. `Gunawan Prakoso` dan `Melati Anggun` masing-masing diberi sesi-produk Fixed Asset Active lewat API sehingga 2 seat terpakai dan kuota penuh
    4. `Rina Wijaya` klik card Fixed Asset di Portal — Product Hub pada Browser A → Popup "Concurrent session limit reached" (event `Concurrent limit reached` pada Fixed Asset)
  - TC-AUTH-SES-289: `Ayu Wijaya` (`ayuwijaya+{runId}-061@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A; format tanggal dan zona waktu Client Alpha Logistik di `Global Settings > General Settings` diset ke nilai non-default (nilai konkret dipilih dari opsi General Settings dan ditulis di fixture `fixtures/auth-session-management.json`; fixture belum ada)
  - TC-AUTH-SES-287: `Citra Nugroho` (`citranugroho+{runId}-061@qwertysystem.net`), Client Alpha Logistik dengan Position `Finance Manager`, Division `Finance`, dan Employee ID terisi; Position `HR Business Partner` tersedia di master Position Client Alpha Logistik; sesi web Active di Browser A
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook): Browser Admin dengan akun aktor Total Control (Global Settings) di atas, dipakai membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log` dan mengubah Position di `Global Settings > User > Edit` untuk Client Alpha Logistik; Browser Admin Q2 dengan akun aktor Total Control (Global Settings) scope Client Q2 (Tabel Data Uji Pre-setup #26), dipakai membaca `Activity Log > Session` milik Fixed Asset dan `Global Settings > Activity Log > Session` untuk `Rina Wijaya` (TC-AUTH-SES-215); Browser A memuat sesi web seed milik user TC yang sedang berjalan.
- State global yang diubah dan dipulihkan: format tanggal dan zona waktu General Settings Client Alpha Logistik (TC-AUTH-SES-289). Hook `after` mengembalikan format tanggal dan zona waktu ke nilai sebelum seeding walau spec gagal di tengah.
- Suite berjalan serial (`parallel: false`); state global yang diubah: format tanggal dan zona waktu General Settings Client Alpha Logistik, dipulihkan di hook `after`.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A, Browser Admin, dan Browser Admin Q2, hapus ketujuh user dan kedua user seed seat, akhiri sesi-produk seed seat Client Q2. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: tiga konteks browser (Browser A, Browser Admin, dan Browser Admin Q2) dengan user agent yang dapat ditetapkan (Chrome on Windows); seeding sesi tanpa info device dan alamat IP (disediakan tim BE); mengakhiri sesi-produk Global Settings dan Fixed Asset milik `Rina Wijaya` lewat API tanpa mengakhiri sesi platform (disediakan tim BE, TC-AUTH-SES-215); pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji pada Browser A untuk TC yang melakukan Log Out; akun aktor di Browser Admin; akun aktor Total Control scope Client Q2 di Browser Admin Q2.

## Test Steps

### TC-AUTH-SES-213: Kolom dan format surface GS Activity Log > Session untuk event sesi

1. Di Browser Admin buka `Global Settings > Activity Log > Session` lalu cari entri `Nur Nugroho`
2. Periksa kolom dan nilai Status pada entri `Nur Nugroho`
3. Verifikasi Kolom tampil berurutan: Date | User | Employee ID | Position | Division | Activity | Status | Note | IP Address | Device / Browser
4. Verifikasi Status tampil `—` untuk entri Activity `Logout`
5. Verifikasi Status tampil `—` untuk entri Activity `Session`
6. Verifikasi Hanya Activity `Login` dan `Reset Password` yang tampil Success atau Failed (entri Activity `Login` milik `Nur Nugroho` tampil Success)
7. Verifikasi Device / Browser berformat `[Browser] on [OS]` (mis. `Chrome on Windows`)

### TC-AUTH-SES-214: User Log menampilkan event platform dan produk dengan suffix nama produk

8. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Agus Maulana`
9. Verifikasi User Log memuat event platform dan event sesi-produk tanpa filter produk
10. Verifikasi Note event sesi-produk Fixed Asset bersuffix `Session started (Fixed Asset)`
11. Verifikasi Note event sesi-produk Global Settings bersuffix `Session started (Global Settings)`
12. Verifikasi Kolom tampil: Date | Activity | Status | Note | IP Address | Device / Browser

### TC-AUTH-SES-249: Info device atau alamat IP kosong ditampilkan sebagai strip di surface log

13. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri `Lestari Wibowo`
14. Verifikasi Kolom Device / Browser menampilkan `—`
15. Verifikasi Kolom IP Address menampilkan `—`

### TC-AUTH-SES-215: Event platform tidak muncul di Session produk dan Concurrent limit reached tidak muncul di GS Session

16. Beralih ke Browser Admin Q2 (akun aktor Total Control (Global Settings) scope Client Q2, Tabel Data Uji Pre-setup #26)
17. Di Browser Admin Q2 buka `Activity Log > Session` milik Fixed Asset dan cari entri `Rina Wijaya`
18. Verifikasi `Activity Log > Session` milik Fixed Asset hanya memuat event sesi-produk (`Session started`, `Session ended`, `Concurrent limit reached`, `Logged out by admin`)
19. Verifikasi `Activity Log > Session` milik Fixed Asset tidak memuat `Logged out`, `Session expired`, dan `Account deleted`
20. Di Browser Admin Q2 buka `Global Settings > Activity Log > Session` dan cari entri `Rina Wijaya`
21. Verifikasi `Global Settings > Activity Log > Session` memuat event platform
22. Verifikasi `Global Settings > Activity Log > Session` memuat `Session started`/`Session ended` Global Settings
23. Verifikasi `Global Settings > Activity Log > Session` tidak memuat `Concurrent limit reached`

### TC-AUTH-SES-288: Kolom Employee ID, Position, atau Division kosong ditampilkan sebagai strip

24. Di Browser A (sesi web Active `Yoga Maulana`, Chrome on Windows) klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
25. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri `Yoga Maulana`
26. Verifikasi Kolom Employee ID, Position, dan Division menampilkan `—`

### TC-AUTH-SES-289: Kolom Date surface log mengikuti format tanggal dan zona waktu General Settings

27. Tutup konteks Browser A sebelumnya (hapus sesi login browser), buka konteks baru Browser A dengan memuat sesi web seed milik `Ayu Wijaya` (Chrome on Windows)
28. Di Browser A klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
29. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri `Ayu Wijaya`
30. Verifikasi Kolom Date menampilkan tanggal dan waktu sesuai format dan zona waktu yang dikonfigurasi di `Global Settings > General Settings` Client Alpha Logistik (nilai non-default dari fixture)

### TC-AUTH-SES-287: Row log menyimpan snapshot Position: perubahan Position tidak mengubah baris lama

31. Tutup konteks Browser A sebelumnya (hapus sesi login browser), buka konteks baru Browser A dengan memuat sesi web seed milik `Citra Nugroho` (Chrome on Windows)
32. Di Browser A klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
33. Di Browser Admin buka `Global Settings > User`, cari `Citra Nugroho`, buka Edit, ubah Position dari `Finance Manager` menjadi `HR Business Partner`, lalu klik [Save]
34. Di Browser A login ulang dengan email `citranugroho+{runId}-061@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
35. Di Browser A klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
36. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari dua entri `Logged out` milik `Citra Nugroho` lewat Note dan email `citranugroho+{runId}-061@qwertysystem.net`, hanya entri yang dibuat sesudah langkah 32 dimulai (dibedakan dari entri seeding lewat stempel waktu)
37. Verifikasi Entri pertama menampilkan Position `Finance Manager` (snapshot saat event)
38. Verifikasi Entri kedua menampilkan Position `HR Business Partner`
39. Verifikasi Kolom Employee ID dan Division terisi sesuai snapshot masing-masing (Division `Finance`)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: struktur dan format surface log, dibaca lewat akun aktor di Browser Admin. Spec ini memuat satu TC objek-uji ringan sesuai `P-5` (b): TC-AUTH-SES-289 (state tenant: format tanggal dan zona waktu General Settings, kelas h), dan TC-AUTH-SES-215 (asersi bahwa event tertentu tidak muncul di surface tertentu; ini asersi isolasi surface/kepemilikan log, bukan absence pencatatan kelas g).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 213, 214, 249, 288, 215, 289, 287 (urutan TC sumber 213, 214, 215, 249, 287, 288, 289). TC yang hanya membaca (213, 214, 249, 215) di awal, TC yang memicu Log Out (288, 289, 287) sesudahnya. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Spec ini memuat 39 langkah karena tujuh TC granular dengan user seed masing-masing dikelompokkan dalam satu suite surface log; tiap TC berdiri sendiri sehingga tidak dipecah.
- TC-AUTH-SES-215 (langkah 17 sampai 19): kolom Dependensi TC bertanda `[DEFERRED]` untuk surface `Activity Log > Session` milik Fixed Asset; langkah membacanya bergantung pada surface itu tersedia (forward-dependency, PRD §12 #3, NC-15).
- TC-AUTH-SES-216 (kegagalan penulisan log tidak membatalkan Log Out) ada di spec `TC-AUTH-SES-E2E-072`.
- Pembagian TC lintas spec (prinsip 10): pencatatan fungsional untuk Logged out dan Session started/ended diuji di spec `TC-AUTH-SES-E2E-056` sampai `059`; spec ini mengasersi struktur, kolom, dan format.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar Browser A, Browser Admin, dan Browser Admin Q2; penutupan konteks Browser A TC sebelumnya (S-09); mencari entri di surface log. Entri "baru" dibedakan dari entri seeding lewat stempel waktu.
- Temuan untuk QA:
  - TC-AUTH-SES-213 Expected butir b menyebut Activity `Reset Password` yang tampil Success atau Failed, tetapi precondition tidak menyiapkan entri `Reset Password`; spec hanya mengasersi entri Activity `Login` milik user seed.
  - TC-AUTH-SES-215 precondition menyebut user "pernah diblok concurrent" di Client Alpha (kuota 5) tanpa menjelaskan seat penuh dan tanpa urutannya, dan tidak menyebut bahwa `Rina Wijaya` harus membuka Global Settings supaya `Session started`/`Session ended` Global Settings ada di `Global Settings > Activity Log > Session` (Expected b); spec memakai Client Q2 (kuota 2) dengan urutan seed di Prerequisites (Rina membuka Global Settings dan Fixed Asset, sesi-produknya diakhiri, dua user seed mengisi 2 seat, lalu Rina diblok) karena Rina tidak bisa memegang sesi-produk Fixed Asset sekaligus diblok saat kuota 2 sudah penuh. Expected tidak menyebut entri `Logged out`, `Session expired`, atau `Account deleted` apa yang seharusnya ada di GS Session; spec membatasi pencarian ke entri `Rina Wijaya`.
  - TC-AUTH-SES-289 tidak menyebut nilai format tanggal dan zona waktu non-default; spec mengacu ke fixture yang belum ada (ditandai di Prerequisites). Mengubah General Settings Client Alpha Logistik memengaruhi tampilan tanggal user lain di Client yang sama selama spec berjalan.
  - TC-AUTH-SES-287 tidak menyebut cara Position `HR Business Partner` disiapkan; spec mensyaratkannya ada di master Position (Prerequisites). TC memakai "Edit" tanpa menyebut tombol simpan; spec memakai `[Save]` mengikuti konvensi form Edit (`docs/e2e-conventions.md` bagian 9).
  - TC-AUTH-SES-249 dan 288 tidak menyebut aktivitas log yang harus dicari; spec mencari entri milik user tersebut tanpa menetapkan Activity tertentu.
  - TC-AUTH-SES-249 precondition b mengutip Tabel Data Uji Pre-setup #18 (Layanan Uji) untuk sesi tanpa info device dan alamat IP, padahal baris itu tidak mendefinisikan seed sesi; spec menulis mekanisme seed sebagai kemampuan yang disediakan tim BE tanpa mengarang endpoint.
  - TC-AUTH-SES-215 membaca dan menyiapkan user milik Client Q2; spec memakai akun aktor Total Control scope Client Q2 (Tabel Data Uji Pre-setup #26) dan user seed seat bersuffix `-061` supaya user bersama Pre-setup #7 tidak berubah.
  - Kolom "User" pada TC-AUTH-SES-213 ada di GS Session tetapi tidak ada di User Log (PRD §8 surface #3); spec mengasersinya hanya di surface yang memilikinya.
