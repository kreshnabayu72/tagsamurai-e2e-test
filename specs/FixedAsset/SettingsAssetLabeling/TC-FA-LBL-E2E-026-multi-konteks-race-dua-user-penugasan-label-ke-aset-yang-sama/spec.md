---
id: TC-FA-LBL-E2E-026-multi-konteks-race-dua-user-penugasan-label-ke-aset-yang-sama
title: "Multi-konteks: race dua user menugaskan label yang sama ke aset yang sama"
priority: Medium
caseType: Edge
status: draft
sourceRules:
  - E-FALB-04
  - F-FALB-11.k2
coverage:
  web: automated
---

# Multi-konteks: race dua user menugaskan label yang sama ke aset yang sama

## Prerequisites

- Mode: FE+BE
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`) sebagai sesi UI dan sesi API pertama; akun Total Control `DU-31` (env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`) sebagai sesi API kedua.
- Login `DU-01` di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini membersihkan data milik spec.
- Data uji: `DU-26` (satu aset Active bersuffix `{runId}-026`); `DU-50` (label seed milik spec, `Assign-{runId}-026`, dibuat lewat API di hook `before` dan dihapus di hook `after`).
- Kemampuan teknis: sesi API aktor `DU-01` dan `DU-31` (login API password; token tidak dihitung sebagai sesi web) untuk request penempelan label ke aset yang dieksekusi API modul aset, dan fixture BE untuk seeding label dan aset serta membaca jumlah relasi aset dengan label (semuanya disediakan tim FE/BE).
- State global: spec membuat satu label dan satu aset; hook `after` melepas relasi, menghapus aset, lalu menghapus label lewat fixture BE.

## Test Steps

### E-FALB-04: Dua user menugaskan label yang sama ke aset yang sama secara simultan

1. Kirim dua request penempelan label seed `DU-50` ke aset `DU-26` secara serentak: satu lewat sesi API `DU-01` dan satu lewat sesi API `DU-31`, hingga kedua respons diterima.
2. Verifikasi kedua respons sukses (kedua pengguna menerima respons sukses).
3. Verifikasi lewat fixture BE pasangan aset `DU-26` dan label seed `DU-50` tersimpan tepat satu relasi.
4. Ketik Search label seed `DU-50`, tekan Enter.
5. Verifikasi baris label seed `DU-50` menampilkan Total Asset 1.

### F-FALB-11.k2: Attach ulang idempoten

6. Kirim ulang request penempelan label seed `DU-50` yang sama ke aset `DU-26` lewat sesi API `DU-01`, hingga respons diterima.
7. Verifikasi respons sukses.
8. Verifikasi lewat fixture BE pasangan aset `DU-26` dan label seed `DU-50` tetap tepat satu relasi (relasi existing tidak berubah).
9. Ganti isi kotak search dengan label seed `DU-50`, tekan Enter.
10. Verifikasi baris label seed `DU-50` masih menampilkan Total Asset 1.

## Notes

- Dua sesi pelaku adalah sesi API: request langsung tidak melewati browser, sehingga hanya respons server dan state data (fixture BE dan kolom Total Asset di UI) yang diasersi (bagian 8b butir 1).
- Klausa `E-FALB-04` "percobaan kedua tidak mengubah apa pun" diamati sebagai jumlah relasi yang tetap satu (langkah 3 dan 5) dan idempotensi attach ulang (langkah 6 sampai 10); urutan commit kedua request tidak dapat dibedakan dari luar.
- Langkah penghubung (S-03): langkah 4 dan 9 (Search untuk menemukan baris target, R-16; langkah 9 mengganti isi kotak yang sudah berisi).
- Asset Detail tidak dibuka di spec ini: aksi penugasan dieksekusi API modul aset dan UI Asset Detail dimiliki PRD modul aset, sehingga hasil attach dibaca lewat fixture BE.
- Pembanding (S-03): `Verifikasi` Total Asset 1 pada langkah 5 dan 10 adalah pembanding tambahan di UI; teks `E-FALB-04` dan `F-FALB-11.k2` tidak menyebut kolom Total Asset.
