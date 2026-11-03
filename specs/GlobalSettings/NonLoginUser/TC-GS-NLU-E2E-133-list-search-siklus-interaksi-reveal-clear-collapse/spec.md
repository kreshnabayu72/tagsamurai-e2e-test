---
id: TC-GS-NLU-E2E-133-list-search-siklus-interaksi-reveal-clear-collapse
title: "List Search: siklus interaksi reveal, clear, dan collapse kotak Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-259
coverage:
  web: automated
---

# List Search: siklus interaksi reveal, clear, dan collapse kotak Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Rina Marlina` dan `Budi Kurniawan`. Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan fokus input dan tooltip hover pada icon Search.
- State global: tidak ada yang diubah. State tabel (Search) kembali kosong pada langkah terakhir. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-259: Siklus interaksi Search List: reveal, clear, collapse

1. Klik icon Search
2. Verifikasi input Search melebar
3. Verifikasi kursor fokus di input Search
4. Verifikasi tooltip `Search`
5. Ketik `Rina` (belum tekan Enter)
6. Verifikasi tabel belum tersaring: sedikitnya satu baris selain `Rina Marlina` masih tampil
7. Tekan Enter
8. Verifikasi tabel tersaring: baris `Rina Marlina` tampil dan baris `Budi Kurniawan` tidak tampil
9. Klik `(✕)`
10. Verifikasi teks di kotak Search kosong
11. Verifikasi tabel belum reset: baris `Rina Marlina` masih tampil dan baris `Budi Kurniawan` tidak tampil
12. Tekan Enter pada input kosong
13. Verifikasi tabel reset: sedikitnya satu baris selain `Rina Marlina` tampil
14. Ketik `Rina`, tekan Enter
15. Klik panah `(←)`
16. Verifikasi kotak Search menutup
17. Verifikasi tabel langsung reset: sedikitnya satu baris selain `Rina Marlina` tampil

## Notes

- Pembagian TC lintas spec: TC-GS-NLU-259 ada di spec ini; TC Search lain ada di spec 076 dan 077.
- Asersi tambahan (S-03): baris `Rina Marlina` dan `Budi Kurniawan` dipakai sebagai anchor positif untuk asersi absence dan "tersaring" (bagian 8b butir 2); `sedikitnya satu baris selain Rina Marlina` dipakai sebagai pembanding "tabel belum tersaring" dan "tabel reset" karena TC tidak menyebut baris tertentu.
- Mode FE+BE: hasil Search dibaca dari backend nyata; tidak ada intercept.
- Temuan untuk QA:
  - Expected a ("tooltip Search") tidak menyebut cara memunculkan tooltip; spec mengasersinya segera setelah klik icon Search ketika kursor masih berada di atas icon (bagian 8b butir 5).
  - Posisi baris pada halaman 1 bergantung pada urutan default Name A-Z dan populasi Pre-setup.
