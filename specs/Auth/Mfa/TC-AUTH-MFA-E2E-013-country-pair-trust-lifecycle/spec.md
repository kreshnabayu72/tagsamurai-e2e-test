---
id: TC-AUTH-MFA-E2E-013-country-pair-trust-lifecycle
title: Siklus Country Pair Trust dari pasangan baru akumulasi frekuensi hingga decay
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-19
  - TC-AUTH-MFA-20
  - TC-AUTH-MFA-21
  - TC-AUTH-MFA-22
coverage:
  web: automated
---

# Siklus Country Pair Trust dari pasangan baru akumulasi frekuensi hingga decay

## Prerequisites

- Mode: FE+BE
- Akun aktif yang melakukan perjalanan rutin antara Negara A dan Negara B

## Test Steps

### Pasangan Negara Baru (Frekuensi = 1)
1. Lakukan login dari Negara B (sebelumnya Negara A)
2. Verifikasi entri `known_country_pair` terbentuk dengan `frequency = 1` dan `is_trusted = false`
3. Verifikasi MFA tetap wajib karena pasangan negara belum berstatus trusted

### Kunjungan Kedua (Frekuensi = 2)
4. Lakukan login kedua dari pasangan negara yang sama
5. Verifikasi nilai `frequency = 2` dan `is_trusted` masih bernilai `false` (MFA tetap wajib)

### Kunjungan Ketiga Dalam 90 Hari (Mencapai Trust)
6. Lakukan login ketiga dalam jendela 90 hari
7. Verifikasi `frequency = 3` dan status `is_trusted` berubah menjadi `true`
8. Verifikasi pada login berikutnya dari pasangan negara ini, dimensi negara tidak lagi memicu MFA

### Peluruhan Trust Pasca >180 Hari (Decay)
9. Simulasikan perpindahan waktu di mana pasangan negara tidak muncul >180 hari (`last_seen_at` >180 hari)
10. Lakukan login kembali dari negara tersebut
11. Verifikasi status `is_trusted` di-reset menjadi `false` dan frekuensi dihitung ulang dari awal

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-13`
- Merepresentasikan `TC-AUTH-MFA-19`, `20`, `21`, `22` (FE Ref: `TC-AUTH-MFA-FE-13`).
