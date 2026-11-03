---
id: TC-AC-ACC-E2E-126-double-klik-konfirmasi-lintas-aksi-tulis
title: "Double-klik Tombol Konfirmasi Aksi Tulis (Suspend, Resend, Save, Delete) Tidak Memproses Ganda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-458
coverage:
  web: automated
---

# Double-klik Tombol Konfirmasi Aksi Tulis (Suspend, Resend, Save, Delete) Tidak Memproses Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Dinamis milik spec (dibuat lewat API di hook `before`, kemampuan seeding disediakan tim FE/BE; nama bersuffix unik sehingga baseline log nol): `PT Dbl Suspend {runId}-126` (Active), `PT Dbl Resend {runId}-126` (Active, FAMS Active, Default User Not Yet Activated), `PT Dbl Save {runId}-126` (Active, PIC Name awal `Budi Hartono`), dan `PT Dbl Delete {runId}-126` (Active, tanpa riwayat subscription dan tanpa user ber-App Access). Hook `after` menghapus sisa Client lewat API.
- Nilai uji: PIC Name hasil Edit `Rina Kartika`.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-458: Double-klik pada aksi tulis (Suspend, Delete, Resend, Save) tidak memproses ganda

1. Ketik Search `PT Dbl Suspend {runId}-126`, tekan Enter
2. Klik `[⋯]` pada baris `PT Dbl Suspend {runId}-126` → pilih `Suspend`
3. Klik `[Suspend]` dua kali cepat
4. Verifikasi toast "Success, client has been suspended." tampil satu kali
5. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Dbl Suspend {runId}-126` lalu tekan Enter
6. Verifikasi tepat satu baris Action `Suspend` untuk "PT Dbl Suspend {runId}-126"
7. Tutup modal Changelog
8. Klik Company Name `PT Dbl Resend {runId}-126` lewat Search (ketik Search `PT Dbl Resend {runId}-126`, tekan Enter)
9. Klik `[Resend Activation Email]` dua kali cepat
10. Verifikasi toast "Success, activation email has been sent." tampil satu kali
11. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Dbl Resend {runId}-126` lalu tekan Enter
12. Verifikasi tepat satu baris Action `Resend Activation Email` untuk "PT Dbl Resend {runId}-126"
13. Tutup modal Changelog
14. Ketik Search `PT Dbl Save {runId}-126`, tekan Enter
15. Klik `[⋯]` pada baris `PT Dbl Save {runId}-126` → pilih `Edit`
16. Ubah PIC Name menjadi `Rina Kartika`
17. Tunggu toast lama hilang
18. Klik `[Save]` dua kali cepat
19. Verifikasi toast "Success, client has been updated." tampil satu kali
20. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Dbl Save {runId}-126` lalu tekan Enter
21. Verifikasi tepat satu baris Action `Edit` Field `PIC Name` untuk "PT Dbl Save {runId}-126"
22. Tutup modal Changelog
23. Ketik Search `PT Dbl Delete {runId}-126`, tekan Enter, sub-tab Active
24. Klik `[⋯]` pada baris `PT Dbl Delete {runId}-126` → pilih `Delete`
25. Ketik nama persis `PT Dbl Delete {runId}-126` pada input "Type the client name to confirm" dan centang "I understand this action cannot be undone"
26. Tunggu toast lama hilang
27. Klik `[Delete]` dua kali cepat
28. Verifikasi toast "Success, client has been deleted." tampil satu kali
29. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Dbl Delete {runId}-126` lalu tekan Enter
30. Verifikasi tepat satu baris Action `Delete` untuk "PT Dbl Delete {runId}-126"
31. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`.
- Spec ini melewati sekitar 35 langkah (di atas smell) karena satu TC menuntut empat aksi tulis (Suspend, Resend, Save, Delete) yang masing-masing butuh dataset dan pembacaan Changelog sendiri; keempat blok satu kelas harness (double-klik), memakai Client bersuffix milik spec, dan Delete ditaruh paling akhir (prinsip 5).
- Langkah penghubung (tanpa awalan Verifikasi): penutupan modal Changelog, "Tunggu toast lama hilang" sebelum klik ganda yang hitungan toast-nya diasersi (R-12), dan Search yang menemukan baris target.
- "Satu set log" pada Expected dibaca sebagai tepat satu baris Action per aksi dengan nama Client bersuffix unik (baseline nol, S-12).
- Post Condition TC-AC-ACC-458: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-458 tidak menyebut data Client, nilai Edit, maupun toast; spec memakai Client bersuffix yang di-seed lewat API (S-06, S-13), nilai PIC Name `Rina Kartika` dari TC lain (TC-AC-ACC-628), dan toast sukses sesuai teks baku function yang dipakai TC lain ("Success, client has been updated.").
  - TC-AC-ACC-458 menyebut Save (Edit) yang objek ujinya milik Create/Edit; TC ini hanya mengasersi satu eksekusi dan satu baris Changelog `Edit`.
