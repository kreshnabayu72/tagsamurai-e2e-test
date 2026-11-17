---
id: TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code
title: "Edit Class Name, Description, dan Class Code Asset Class lalu Save"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-171
  - TC-FA-FAAC-172
  - TC-FA-FAAC-174
  - TC-FA-FAAC-175
sourceRules: ["T-03", "F-FAAC-02.k2", "V-04", "T-02", "F-FAAC-02.k18", "FAAC-LOGIC-10b", "FAAC-LOGIC-07i"]
smoke: []
dependsOn: []
trace:
  "T-03": 4
  "F-FAAC-02.k2": [5, 6, 7]
  "V-04": [12, 13, 18]
  "T-02": [19, 24]
  "F-FAAC-02.k18": 25
  "FAAC-LOGIC-10b": 26
  "FAAC-LOGIC-07i": [27, 28]
anchor: [14]
coverage:
  web: automated
---

# Edit Class Name, Description, dan Class Code Asset Class lalu Save

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > tab Asset Class). Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-ANCHOR` (Active, Class Name "Anchor Heavy Equipment", Description "Asset class fixture group B"); Asset Class `B-SHARE` (tanpa Asset Name; Class Name dan Description awal sesuai seed). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture `fixtures/fixed-asset-asset-class.json` belum ada, disediakan tim FE).
- Data uji: Class Code "b-anchor" (kode Asset Class lain dengan kapitalisasi berbeda); Class Name "Anchor Heavy Equipment"; Class Name "Shared Account Renamed"; Description "Updated description".
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan data Asset Class lewat fixture BE; kemampuan baca BE untuk Class Code Asset Class dan jumlah entri Changelog, System Log, dan Activity Log (audit trail permanen, N dibaca sebelum aksi, bagian 8b butir 10).
- State global: tidak ada yang diubah selain data Asset Class di atas; pemulihan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-172: Save tanpa perubahan nilai menampilkan toast netral No-Op

1. Baca jumlah entri Changelog, System Log, dan Activity Log sebagai baseline
2. Klik link Class Code "B-ANCHOR" di tabel
3. Klik "Save" tanpa mengubah field apa pun
4. Verifikasi muncul toast info: "No changes to save."
5. Verifikasi halaman kembali ke tabel Asset Class
6. Verifikasi baris B-ANCHOR tetap menampilkan Class Name "Anchor Heavy Equipment" (tidak ada data berubah)
7. Verifikasi jumlah entri Changelog, System Log, dan Activity Log sama dengan baseline langkah 1 (selisih 0)

### TC-FA-FAAC-174: Ubah Class Code menjadi kode Asset Class lain ditolak

8. Klik link Class Code "B-SHARE" di tabel
9. Ubah Class Code menjadi "b-anchor"
10. Baca jumlah entri Changelog, System Log, dan Activity Log sebagai baseline
11. Klik "Save"
12. Verifikasi caption "Class code already exists" pada Class Code
13. Verifikasi Class Code Asset Class B-SHARE di server tetap "B-SHARE" (tidak ada data tersimpan)
14. Verifikasi jumlah entri Changelog, System Log, dan Activity Log sama dengan baseline langkah 10 (selisih 0)
15. Kembalikan Class Code ke "B-SHARE"

### TC-FA-FAAC-175: Edit Class Name menjadi sama dengan Asset Class lain diizinkan

16. Ubah Class Name menjadi "Anchor Heavy Equipment"
17. Klik "Save"
18. Verifikasi tidak ada caption error pada form
19. Verifikasi muncul toast sukses: "Success, asset class has been updated."

### TC-FA-FAAC-171: Edit Class Name dan Description lalu Save

20. Klik link Class Code "B-SHARE" di tabel
21. Pada tab General ubah Class Name menjadi "Shared Account Renamed"
22. Ubah Description menjadi "Updated description"
23. Klik "Save"
24. Verifikasi muncul toast sukses di tabel Asset Class: "Success, asset class has been updated."
25. Verifikasi halaman kembali ke tabel Asset Class
26. Verifikasi baris B-SHARE menampilkan Class Name "Shared Account Renamed"
27. Verifikasi tidak muncul Dialog Apply Changes
28. Verifikasi perubahan General berlaku langsung tanpa Effective From: tidak ada pilihan Effective From pada proses Save

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 172, 174, 175, 171 (kasus tanpa perubahan dan penolakan lebih dulu, lalu Save berhasil pada B-SHARE; TC-175 mengubah Class Name B-SHARE sehingga TC-171 memulai dari nilai itu).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class `B-ANCHOR` dan `B-SHARE` adalah seed bertanda `B-*` per TC; nama dipakai apa adanya dan pemulihannya dijamin fixture BE yang disediakan tim FE/BE.
- Langkah penghubung (S-03): langkah 1, 10 (baseline audit trail, S-12); langkah 15 (pemulihan Class Code form dirty, S-09). Langkah 16 melanjutkan form B-SHARE yang sama sesudah pemulihan; blok TC-175 tidak membuka ulang form.
- S-05: Expected TC-172 dan TC-174 "tidak ada entri/log" diasersi sebagai selisih jumlah entri terhadap baseline pada Changelog, System Log, dan Activity Log (kemampuan baca BE); ini asersi jumlah, bukan kelas g.
- Temuan untuk QA: TC-171 tidak menyebut Class Name dan Description awal B-SHARE; TC-171 mensyaratkan "belum dipakai aset" dan tidak ada langkah observasi untuk Post Condition (tidak diasersi).
