---
id: TC-GS-USER-E2E-031-pair-unpair-tag
title: Pasang, ganti, dan lepas TAG RFID user
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-59
  - TC-GS-USER-64
  - TC-GS-USER-437
  - TC-GS-USER-436
  - TC-GS-USER-63
coverage:
  web: automated
---

# Pasang, ganti, dan lepas TAG RFID user

## Prerequisites

- Login sebagai Role: Total Control, entity Client pada plan Growth atau lebih tinggi (Scan TAG tampil)
- User "Oscar Ramadhan" tanpa TAG terpasang
- TAG RFID "TAG A" dan "TAG B": keduanya sudah diaktivasi sebagai User TAG, belum dipasang ke user mana pun, dan belum pernah dipakai
- Simulasi scan RFID: skrip bisa memasukkan kode TAG seolah hasil scan hardware. Kebutuhan ini disediakan tim FE
- Spec ini memasang TAG ke "Oscar Ramadhan" lalu melepasnya di akhir, jadi TAG A dan TAG B kembali bebas

## Test Steps

### Pair dari User Detail

1. Buka User Detail "Oscar Ramadhan"
2. Verifikasi sub-section User TAG menampilkan badge "Unverified" dan tombol `Scan TAG`, tanpa tombol `Unpair`
3. Klik `Scan TAG` lalu scan "TAG A"
4. Verifikasi toast "Success, TAG has been paired." muncul
5. Verifikasi badge berubah menjadi "Verified", kode TAG A tampil, dan tombol berubah menjadi `Scan TAG` dan `Unpair`

### Ganti TAG dari Modal Edit

6. Buka Modal Edit "Oscar Ramadhan"
7. Verifikasi field TAG langsung menampilkan status paired dengan badge "Verified" dan kode TAG A
8. Klik `Scan TAG` lalu scan "TAG B"
9. Verifikasi badge tetap "Verified" dan tidak sempat menjadi "Unverified", dan kode TAG B menggantikan TAG A
10. Klik `[Save]`
11. Verifikasi kode TAG pada "Oscar Ramadhan" sekarang TAG B, dan TAG A tidak lagi terpasang ke user mana pun

### Lepas TAG dari User Detail

12. Buka User Detail "Oscar Ramadhan"
13. Klik `Unpair`
14. Verifikasi dialog "Unpair TAG from this user?" muncul
15. Klik `[Cancel]` pada dialog
16. Verifikasi dialog tertutup tanpa efek, badge tetap "Verified", tombol `Unpair` tetap tampil, dan tidak ada entri Changelog baru
17. Klik `Unpair` lagi lalu konfirmasi pada dialog
18. Verifikasi toast "Success, TAG has been unpaired." muncul
19. Verifikasi badge kembali "Unverified" dan hanya tombol `Scan TAG` yang tampil (tanpa `Unpair`)

## Notes

- Spec ini butuh simulasi scan hardware. Dipisah dari spec lain supaya kegagalan hardware tidak menutupi hasil spec lain.
- `TC-GS-USER-59` dan `TC-GS-USER-64` sama-sama menguji pair dari Detail sampai badge menjadi Verified, sehingga digabung di langkah 3 sampai 5.
- Pair di modal Create dicakup `TC-GS-USER-E2E-004-create-user-scan-pair-tag`.
- Validasi TAG yang ditolak dicakup `TC-GS-USER-E2E-032-validasi-scan-tag`.
- Perubahan TAG dari Modal Edit bersifat staged sampai `[Save]`, sedangkan dari User Detail instan dengan toast sendiri.
