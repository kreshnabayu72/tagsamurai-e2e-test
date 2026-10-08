---
id: TC-GS-GSET-E2E-011-save-happy-path-dan-boundary-idle
title: Save sukses dan boundary Session Idle Timeout 8 hours
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-25
  - TC-GS-GSET-152
coverage:
  web: automated
---

# Save happy path dan boundary Session Idle Timeout 8 hours

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data uji: `Currency => IDR`, `Time Zone => (UTC+07:00) Bangkok, Hanoi, Jakarta`,
  `Session Idle Timeout => 30 minutes`, `Date Format => dd/MM/yy`, `Time Format => HH:mm`.
- Hook menyiapkan lingkungan bersih sehingga perubahan tersimpan bisa diverifikasi tanpa tumpang tindih
  spec lain. Setelah spec selesai, `after` mengembalikan `Session Idle Timeout` ke `30 minutes`.

## Test Steps

### Save sukses standar

1. Buka halaman `Global Settings > General Settings`
2. Ubah `Session Idle Timeout` menjadi `1 hour`
3. Klik `[Save]`
4. Verifikasi tombol `[Save]` menampilkan indikator proses/progress
5. Verifikasi toast sukses `Success, general settings has been saved.` tampil
6. Verifikasi tombol `[Save]` menjadi non-aktif kembali
7. Muat ulang halaman
8. Verifikasi `Session Idle Timeout` tetap `1 hour` (persist tersimpan)

### Save tanpa perubahan tidak diizinkan

9. Dengan data sudah tersimpan, verifikasi tombol `[Save]` non-aktif dan tidak dapat diklik

### Boundary maksimum: Session Idle Timeout 8 hours

10. Ubah `Session Idle Timeout` menjadi `8 hours`
11. Klik `[Save]`
12. Verifikasi toast sukses tampil
13. Verifikasi nilai tersimpan `8 hours` setelah muat ulang
14. Uji tambahan: pastikan nilai `8 hours` dibaca & dirender sebagai `8 hours` (bukan `480 minutes`)
    dan diberikan refetch saat halaman dibuka kembali

### Boundary nilai terkecil + gabungan field lain

15. Ubah `Session Idle Timeout` menjadi `15 minutes`, `Date Format` menjadi `M/d/yy`, dan
    `Time Format` menjadi `hh:mm a`
16. Klik `[Save]`, verifikasi toast sukses
17. Muat ulang halaman, verifikasi ketiga nilai tersimpan

## Notes

- DPB `sessionIdleTimeoutBoundary` membuktikan 15 menit (nilai minimum), 8 jam (maksimum), serta
  format read/write yang persis (bukan konversi satuan).
- Resolver `after` mengembalikan `Session Idle Timeout` ke `30 minutes` agar spec lain tidak membaca
  nilai yang telah dimutasi.