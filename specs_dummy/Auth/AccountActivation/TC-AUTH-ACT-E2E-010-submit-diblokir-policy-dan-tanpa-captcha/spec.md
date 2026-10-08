---
id: TC-AUTH-ACT-E2E-010-submit-diblokir-policy-dan-tanpa-captcha
title: "Submit diblokir client saat Password Policy belum terpenuhi dan ketiadaan CAPTCHA"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-37
  - TC-AUTH-ACT-45
  - TC-AUTH-ACT-46
  - TC-AUTH-ACT-47
  - TC-AUTH-ACT-48
  - TC-AUTH-ACT-49
  - TC-AUTH-ACT-50
  - TC-AUTH-ACT-51
  - TC-AUTH-ACT-52
  - TC-AUTH-ACT-57
coverage:
  web: automated
---

# Submit diblokir client saat Password Policy belum terpenuhi dan ketiadaan CAPTCHA

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run); user ini akan diaktivasi pada langkah terakhir spec sehingga hook `after` membersihkan user beserta token hasil konsumsi.
- Pemantauan request jaringan (DevTools/network log) untuk memastikan tidak ada request Set Password yang dikirim pada tiap kasus diblokir.
- Akses API read-only untuk memverifikasi status user dan token sebelum serta sesudah spec.

## Test Steps

### Panjang 73 karakter tidak mengirim request (TC-AUTH-ACT-37)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Ketik `Aa1!` diikuti 69 karakter `x` (total 73 karakter) pada field Password dan Confirm Password.
3. Klik button "Set Password" sambil memantau request jaringan.
4. Verifikasi tidak ada request set password yang dikirim ke server.
5. Verifikasi halaman tetap `Auth > Account Activation > Set Password`, pesan "Max. 72 characters" tetap tampil, tidak ada toast, dan Password Policy tidak mengalami perubahan akibat klik.

### Password melanggar satu per satu aturan policy (TC-AUTH-ACT-45 s.d. TC-AUTH-ACT-52)

6. Setel field Password dan Confirm Password `Abcde1!`, lalu klik button "Set Password".
7. Verifikasi tidak ada request yang dikirim, baris "Minimum 8 characters" tetap abu-abu (disabled) + ○, halaman tetap di Set Password, tanpa toast, dan tanpa inline error pada Confirm Password.
8. Setel kedua field menjadi `abcdefg1!`, lalu klik button "Set Password".
9. Verifikasi tidak ada request yang dikirim dan baris "One uppercase (A-Z)" tetap abu-abu + ○ tanpa toast.
10. Setel kedua field menjadi `ABCDEFG1!`, lalu klik button "Set Password".
11. Verifikasi tidak ada request yang dikirim dan baris "One lowercase (a-z)" tetap abu-abu + ○ tanpa toast.
12. Setel kedua field menjadi `Abcdefgh!`, lalu klik button "Set Password".
13. Verifikasi tidak ada request yang dikirim dan baris "One number (0-9)" tetap abu-abu + ○ tanpa toast.
14. Setel kedua field menjadi `Abcdefg1`, lalu klik button "Set Password".
15. Verifikasi tidak ada request yang dikirim dan baris "One special character" tetap abu-abu + ○ tanpa toast.
16. Setel kedua field menjadi `Abcd efg1!` (spasi di tengah), lalu klik button "Set Password".
17. Verifikasi tidak ada request yang dikirim dan baris "Password cannot contain spaces" tetap abu-abu + ○ tanpa toast.
18. Setel kedua field menjadi ` Abcdefg1!` (satu spasi di awal), lalu klik button "Set Password".
19. Verifikasi tidak ada request yang dikirim dan baris "Password cannot contain spaces" tetap abu-abu + ○ tanpa toast.
20. Setel kedua field menjadi `Abcdefg1! ` (satu spasi di akhir), lalu klik button "Set Password".
21. Verifikasi tidak ada request yang dikirim dan baris "Password cannot contain spaces" tetap abu-abu + ○ tanpa toast.

### Submit valid tanpa CAPTCHA (TC-AUTH-ACT-57)

22. Kosongkan kedua field, lalu ketik `Aman#Sandi8` pada field Password dan Confirm Password.
23. Verifikasi tidak ada widget CAPTCHA pada halaman sebelum klik.
24. Klik button "Set Password" tanpa interaksi tambahan.
25. Verifikasi tidak ada pesan captcha belum diselesaikan, submit diproses, dan halaman `Auth > Account Activation > Activation Success` tampil.
26. Verifikasi status user berubah menjadi Activated dan token berstatus Consumed.

## Notes

- Kasus submit yang diblokir tidak mengubah data, sehingga seluruh varian policy berjalan berurutan dalam satu sesi form.
- Ketiadaan CAPTCHA diverifikasi lewat submit valid sebagai langkah terakhir: aksi yang menghabiskan token selalu ditaruh paling akhir sekaligus menjadi cleanup alamiah data seeding spec ini.
- Kebutuhan pemantauan request dan verifikasi status lewat API dicatat di Prerequisites.
