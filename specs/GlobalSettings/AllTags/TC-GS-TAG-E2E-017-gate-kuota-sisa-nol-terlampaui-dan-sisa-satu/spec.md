---
id: TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu
title: "Gate Kuota Activate TAG: Sisa 0 Fail-Fast, Terlampaui (60 of 50), dan Sisa Tepat 1"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-13
  - TC-GS-TAG-39
  - TC-GS-TAG-40
  - TC-GS-TAG-41
coverage:
  web: automated
---

# Gate Kuota Activate TAG: Sisa 0 Fail-Fast, Terlampaui (60 of 50), dan Sisa Tepat 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec ini kelas blokir karena kondisi data (prinsip 12 bagian 3): kuota yang diuji disetel lewat fixture BE (disediakan tim FE/BE) sebelum tiap bagian.
- Akun (dua client; bagian pertama Client Over di hook `before`, ganti akun eksplisit di langkah 9):
  - Total Control Client Over `totalControl_automated_qaOver@qwertysystem.net` (Gunawan Setiadi), `Spectra.env.GS_TC_OVER_PASSWORD`; RFID–Object TAG terpakai 60 dari kuota 50 (60 tag RFID Object non-Retired akibat penurunan alokasi).
  - Total Control Client Quota `totalControl_automated_qaQuota@qwertysystem.net` (Fitri Handayani), `Spectra.env.GS_TC_QUOTA_PASSWORD`; plan Growth; kuota NFC 0 (terpakai 0) untuk TC-39; GPS kuota 3 dengan terpakai 2 (sisa 1) untuk TC-41, disetel fixture BE pada langkah 18.
  - Nama env `GS_TC_OVER_PASSWORD` dan `GS_TC_QUOTA_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example` (lihat `suite.md` bagian Kredensial). Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach` untuk akun aktor pertama; setelah ganti akun layar yang sama dibuka di langkah ganti akun.
- State yang diubah: jumlah terpakai kuota GPS Client Quota (langkah 18); hook `after` memulihkannya ke nilai awal (dicatat di hook `before`) walau spec gagal. Spec tidak melakukan Submit Activation.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-13: Kuota terlampaui tampil apa adanya (Client Over)

1. Verifikasi kartu `RFID – Object TAG` menampilkan `60 of 50`
2. Verifikasi keterangan kartu `0 remaining`
3. Verifikasi tidak ada nilai negatif pada kartu

### TC-GS-TAG-40: Kuota terlampaui (60 of 50) diperlakukan fail-fast

4. Klik `+ Activate TAG`
5. Pilih `RFID – Object TAG`
6. Verifikasi dialog `Insufficient Quota` varian fail-fast muncul
7. Verifikasi halaman Activate TAG tidak terbuka
8. Klik `OK` pada dialog
9. Ganti akun: logout, login sebagai Total Control Client Quota (`Spectra.env.GS_TC_QUOTA_PASSWORD`)
10. Buka Global Settings > TAG > Tab All

### TC-GS-TAG-39: Kuota tipe sisa 0 (NFC): Dialog 1 fail-fast

11. Klik `+ Activate TAG`
12. Pilih `NFC`
13. Verifikasi dialog `Insufficient Quota` dengan body `No quota available for this TAG type. Contact your administrator or request more allocation.`
14. Verifikasi dialog hanya memiliki tombol tunggal `OK`
15. Verifikasi popup `Ready to Activate a TAG` dan halaman Activate TAG tidak pernah terbuka
16. Klik `OK`
17. Verifikasi kembali ke List Tab All

### TC-GS-TAG-41: Sisa kuota tepat 1 membuka sesi

18. Setel kuota GPS Client Quota menjadi 3 dengan terpakai 2 (sisa 1) lewat fixture BE (disediakan tim FE/BE)
19. Muat ulang Global Settings > TAG > Tab All
20. Klik `+ Activate TAG`
21. Pilih `GPS` pada overlay `Select TAG Type`
22. Klik `Continue` pada popup `Ready to Activate a TAG`
23. Verifikasi halaman Activate TAG terbuka dengan tipe GPS terkunci
24. Verifikasi dialog `Insufficient Quota` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: blokir karena kondisi data (prinsip 12 bagian 3) dengan data kuota disetel fixture BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memakai dua akun/client dengan Step ganti akun eksplisit (langkah 9); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah akun kasus b). Total langkah di bawah ~35 sehingga tidak butuh alasan tambahan.
- TC-13 (kartu `60 of 50`) ditempatkan di spec ini bersama gate kuota Activate (Client Over), bukan di spec kartu counter (spec 003); rujukan dua arah dicatat di Notes spec 003.
- Langkah penghubung (tanpa `Verifikasi`): `OK` pada dialog (langkah 8 dan 16) menutup dialog agar langkah berikutnya mulai dari List; langkah 18 menyiapkan precondition TC-41 (`kuota GPS 3, terpakai 2`) dan langkah sesudahnya memuat ulang halaman supaya kartu dan gate membaca kuota baru.
- TC-40 menyebut "Dialog `Insufficient Quota` varian fail-fast" tanpa teks body; spec mengasersi dialog tampil (langkah 6), sedangkan teks body hanya diasersi pada TC-39 (langkah 13).
- Temuan untuk QA:
  - TC-39, TC-40, TC-41 menyetel jumlah terpakai lewat fixture BE tanpa menyebut mekanismenya; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE dan memulihkannya di hook `after`.
  - TC-41 tidak menyebut tindakan sesudah halaman Activate terbuka; sesi tidak diteruskan ke Submit, dan keluar halaman dengan staging kosong ditangani hook `beforeEach` berikutnya.
