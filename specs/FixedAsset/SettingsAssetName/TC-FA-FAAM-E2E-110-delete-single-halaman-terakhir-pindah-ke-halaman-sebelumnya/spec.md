---
id: TC-FA-FAAM-E2E-110-delete-single-halaman-terakhir-pindah-ke-halaman-sebelumnya
title: "Delete Single: Menghapus Baris Terakhir di Halaman Terakhir Pindah ke Halaman Terakhir yang Masih Ada"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-274
coverage:
  web: automated
---

# Delete Single: Menghapus Baris Terakhir di Halaman Terakhir Pindah ke Halaman Terakhir yang Masih Ada

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoPage11` (Pre-setup #15b). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password dari `Spectra.env.FA_PAGE11_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`).
- Data Pre-setup #15b: client `AutoPage11` khusus TC ini berisi tepat 11 Asset Name ber-Total Asset 0 dengan ukuran halaman 10, sehingga halaman 2 berisi satu baris `Last Page Item`. Spec menghapus `Last Page Item`; client dan baris itu disediakan ulang ke keadaan Pre-setup #15b oleh seeding di hook `before` dan `after` (disediakan tim BE/FE; suite berjalan serial; efeknya adalah satu entri Changelog Delete untuk `Last Page Item` pada client itu; S-06).
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-274: Menghapus baris terakhir di halaman terakhir pindah ke halaman terakhir yang masih ada

1. Buka halaman 2
2. Verifikasi halaman 2 aktif dan hanya memuat satu baris `Last Page Item`
3. Klik `⋯` baris `Last Page Item` lalu `Delete`
4. Klik `[Delete]`
5. Verifikasi tabel berpindah ke halaman 1 (halaman terakhir yang masih ada)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`.
- Langkah 2 adalah `Verifikasi` keadaan awal yang dibutuhkan asersi pada langkah 5 (S-14); TC tidak memuatnya sebagai Expected.
- Temuan untuk QA:
  - TC-FA-FAAM-274 memakai client `AutoPage11` (Pre-setup #15b) tetapi akun aktornya dan email-nya tidak tertulis di Pre-setup.
  - TC-FA-FAAM-274 Expected tidak menyebut toast sukses atau hilangnya baris `Last Page Item`; spec hanya mengasersi perpindahan halaman.
