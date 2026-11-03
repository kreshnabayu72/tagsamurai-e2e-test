---
id: TC-AC-DN-E2E-044-create-validasi-batas-karakter-dan-paste
title: "Create Device Name: Batas 120 Karakter (121 Karakter dan Paste 121) dan Paste Dua Baris"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-91
  - TC-AC-DN-583
  - TC-AC-DN-584
coverage:
  web: automated
---

# Create Device Name: Batas 120 Karakter (121 Karakter dan Paste 121) dan Paste Dua Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`).
- Data uji teks (Data Dinamis tanpa record; tidak ada yang tersimpan sehingga tidak bersuffix, panjang tepat sesuai TC):
  - Teks 121 karakter A (TC-AC-DN-91, diketik): `Alat Pemindai Gudang Besar Alat Pemindai Gudang Besar Alat Pemindai Gudang Besar Alat Pemindai Gudang Besar Alat PemindZQ`.
  - Teks 121 karakter B (TC-AC-DN-583, ditempel): `Alat Pemindai Gudang Besar ` diulang hingga tepat 121 karakter.
  - Teks dua baris (TC-AC-DN-584, ditempel): `Smart Gate`, karakter baris baru, lalu `Antenna UHF`.
- Kemampuan teknis: menyalin teks ke clipboard dan menempelnya ke field (TC-AC-DN-583 dan TC-AC-DN-584), termasuk teks yang memuat karakter baris baru; disediakan tim FE.
- Tidak ada record yang dibuat: semua [Submit] ditolak validasi atau tidak mengirim request, sehingga tidak ada cleanup. State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-91: Create dengan Device Name 121 karakter

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik teks 121 karakter A pada field Device Name
3. Verifikasi error inline "Max. 120 characters" muncul langsung saat karakter ke-121 diketik, sebelum klik `[Submit]`
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi error inline "Max. 120 characters" tetap tampil
8. Verifikasi popup form tetap terbuka
9. Verifikasi tidak ada toast

### TC-AC-DN-583: Paste teks 121 karakter

10. Klik `[Clear Field]`
11. Salin teks 121 karakter B ke clipboard, lalu tempel (paste) ke field Device Name
12. Verifikasi error inline "Max. 120 characters" tampil langsung di bawah field Device Name setelah paste, tanpa menunggu `[Submit]`
13. Verifikasi teks tidak dipotong otomatis menjadi 120 karakter (field berisi 121 karakter)
14. Klik `[Submit]`
15. Verifikasi popup form tetap terbuka
16. Verifikasi tidak ada toast

### TC-AC-DN-584: Paste teks dua baris

17. Klik `[Clear Field]`
18. Salin teks dua baris ke clipboard, lalu tempel (paste) ke field Device Name
19. Verifikasi field Device Name menampilkan isi paste dalam satu baris dan tidak memuat karakter baris baru
20. Verifikasi tidak ada pesan error pada field Device Name
21. Klik `[Clear Field]`
22. Klik icon close `[✕]` pada popup

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC-AC-DN-91 bertanda FE Test "Need API"; TC-AC-DN-583 dan TC-AC-DN-584 "UI Only".
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 10 dan 17 (`[Clear Field]` menghapus isian dan error TC sebelumnya, S-09 dan R-12), langkah 21 dan 22 (pemulihan form dirty lalu menutup form kosong tanpa dialog `Unsaved Changes`).
- Langkah 14 pada TC-AC-DN-583 mengklik `[Submit]` dengan Measurement dan Category kosong, mengikuti TC (request tidak dikirim); error wajib diisi untuk kedua field tidak diasersi karena bukan Expected TC itu.
- Teks 121 karakter A dan B tidak bersuffix `{runId}` karena panjangnya harus tepat 121 karakter, tidak pernah tersimpan, dan tidak dipakai asersi absence.
- Temuan untuk QA:
  - Post Condition "Tidak ada record baru tersimpan" (TC-AC-DN-91) dan "Tidak ada Device Name baru tersimpan" (TC-AC-DN-583) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-AC-DN-583 Expected c ("Submit tidak membuat Device Name baru") hanya teramati lewat popup yang tetap terbuka dan tidak adanya toast; tidak ada langkah pengecekan List di TC.
