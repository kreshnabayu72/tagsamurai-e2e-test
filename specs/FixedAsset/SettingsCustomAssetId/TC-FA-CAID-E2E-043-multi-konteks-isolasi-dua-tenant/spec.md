---
id: TC-FA-CAID-E2E-043-multi-konteks-isolasi-dua-tenant
title: "Multi-Konteks: Isolasi Dua Tenant pada Form, Code List, dan Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-310
  - TC-FA-CAID-311
coverage:
  web: automated
---

# Multi-Konteks: Isolasi Dua Tenant pada Form, Code List, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun kedua: Total Control `Company Beta` (Pre-setup No 9); email disediakan tim FE/BE (Pre-setup No 9), password `Spectra.env.FA_BETA_TC_PASSWORD`; ganti akun ditulis sebagai langkah eksplisit dan hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite, termasuk Group `Jakarta Office` (Code `JKT`); `Company Beta` dengan konfigurasi Separator `. (Dot)`, aset `BETA.LAP.T490.0926.1`, dan Group sendiri (No 9). `Company Changelog` (Pre-setup No 15) memiliki tujuh entri seed Changelog Custom Asset ID L1 sampai L7 (Date `15/09/26, 14:25` sampai `10/09/26, 10:00`, Modified By antara lain `Rina P` dan `Sarah J`); dipakai sebagai precondition TC (TC-FA-CAID-311 b) dan hanya dirujuk sebagai entri yang tidak boleh tampil di Company Beta pada langkah 19; Company itu disediakan tim FE/BE dan tidak diubah spec ini.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Modal Changelog: Custom Asset ID `Company Beta` sebelum aksi pada hook `before` lewat sesi API Beta (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Separator Company Alpha menjadi `- (Dash)`. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-310: Save di satu Company tidak mengubah konfigurasi dan Asset ID Company lain

1. Pilih Separator `- (Dash)` pada Company Alpha
2. Klik `[Save]`
3. Tunggu aksi selesai
4. Ganti akun: logout, lalu login sebagai Total Control `Company Beta`
5. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
6. Verifikasi konfigurasi `Company Beta` tetap Separator `. (Dot)`
7. Buka Fixed Asset > Assets > All Assets
8. Verifikasi Asset ID aset `Company Beta` tetap `BETA.LAP.T490.0926.1`
9. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu buka Modal Changelog: Custom Asset ID
10. Verifikasi jumlah entri Modal Changelog `Company Beta` sama dengan baseline sehingga tidak memuat entri milik Company Alpha

### TC-FA-CAID-311: Pengguna Company lain tidak melihat data Company tetangga

11. Tutup Modal Changelog: Custom Asset ID
12. Verifikasi form menampilkan konfigurasi `Company Beta` (Separator `. (Dot)`)
13. Klik `[View Code List]`, lalu buka tab Group Codes
14. Verifikasi tab Group Codes memuat sedikitnya satu baris Group milik `Company Beta`
15. Verifikasi Group `Jakarta Office` tidak tampil di tab Group Codes
16. Tutup Modal View Code List
17. Klik `[Changelog]`
18. Verifikasi jumlah entri Modal Changelog `Company Beta` sama dengan baseline sehingga entri milik Company Alpha tidak tampil
19. Verifikasi entri seed L1 sampai L7 `Company Changelog` (Pre-setup No 15, Date `15/09/26, 14:25` sampai `10/09/26, 10:00`, antara lain Modified By `Rina P` dan `Sarah J`) tidak tampil di Modal Changelog `Company Beta`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 3 (tunggu aksi selesai karena langkah berikutnya ganti akun), langkah 4 (ganti akun), langkah 5, 7, dan 9 (membuka halaman), langkah 11 dan 16 (menutup modal).
- Langkah 6 pada TC-FA-CAID-310 dan langkah 12 pada TC-FA-CAID-311 mengasersi nilai form yang sama pada dua TC karena Expected keduanya menyebutnya.
- Langkah 19 mengasersi Expected c TC-FA-CAID-311 (entri seed L1 sampai L7 tidak tampil), dibedakan dari entri Company Alpha pada langkah 18; langkah 18 sekaligus menjadi anchor positif (jumlah entri dibanding baseline pada surface yang sama, bagian 8b butir 2) untuk absence pada langkah 19.
- Pembagian TC lintas spec: TC-FA-CAID-324, TC-FA-CAID-326, dan TC-FA-CAID-327 ada di spec 044; TC-FA-CAID-328 dan TC-FA-CAID-329 di spec 048; TC-FA-CAID-330 dan TC-FA-CAID-331 di spec 045.
- Temuan untuk QA:
  - Pre-setup No 9 tidak menyebut nama Group `Company Beta`; spec mengasersi keberadaan sedikitnya satu baris Group milik `Company Beta` tanpa menyebut nama.
  - TC-FA-CAID-311 Expected c menyebut entri seed L1 sampai L7 (Pre-setup No 15) "antara lain oleh `Rina P` dan `Sarah J`" tanpa daftar lengkap tiap entri; spec memakai Date dan Modified By yang disebut TC dan menjadikan entri hasil Save TC-FA-CAID-310 sebagai entri Company Alpha (dicakup baseline jumlah, langkah 10 dan 18).
  - TC-FA-CAID-310 Expected c tidak menyebut cara menentukan "entri milik Company Alpha"; spec memakai baseline jumlah entri `Company Beta`.
  - Post Condition TC-FA-CAID-310 dan TC-FA-CAID-311 tidak diasersi karena TC tidak memberi langkah observasinya.
