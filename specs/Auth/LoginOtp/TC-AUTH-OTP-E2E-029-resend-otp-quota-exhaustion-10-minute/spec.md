---
id: TC-AUTH-OTP-E2E-029-resend-otp-quota-exhaustion-10-minute
title: Batas kuota resend ke-5 memicu cooldown 10 menit dan status exhausted permanen
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-52
  - TC-AUTH-OTP-53
  - TC-AUTH-OTP-56
coverage:
  web: automated
---

# Batas kuota resend ke-5 memicu cooldown 10 menit dan status exhausted permanen

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dan user telah melakukan aksi resend sebanyak 4 kali (`resend_count = 4`)
- Countdown antar-resend ke-4 telah selesai sehingga tombol "Resend code" kembali enabled
- Environment testing memiliki kontrol simulasi waktu/clock

## Test Steps

### Eksekusi Resend ke-5 & Pemicu Cooldown 10 Menit

1. Klik tombol "Resend code" untuk yang ke-5 kalinya (`resend_count = 5`)
2. Verifikasi toast notifikasi muncul dengan teks "Success, the code has been sent."
3. Verifikasi tombol "Resend code" berubah menjadi disabled
4. Verifikasi label tombol kini menampilkan hitung mundur selama 10 menit dengan format awal "Resend code in (09:59)" yang berjalan mundur
5. Verifikasi selama masa 10 menit ini, tombol sama sekali tidak dapat diklik

### Status Exhausted Permanen Pasca Cooldown 10 Menit

6. Majukan waktu simulasi sebanyak 10 menit hingga hitung mundur mencapai 00:00
7. Verifikasi setelah 10 menit berakhir, tombol "Resend code" TIDAK berubah menjadi enabled
8. Verifikasi tombol tetap disabled secara permanen dengan teks statis "You have reached the maximum number of resend attempts."
9. Verifikasi melalui Activity Log Session bahwa seluruh pembatasan kuota dan countdown resend ini tidak dicatat ke surface audit log

## Notes

- Kuota resend dibatasi maksimal 5 kali per sesi alur verifikasi. Melewati 5 kali mengunci aksi resend permanen pada sesi tersebut untuk memitigasi SMS/Email flooding.
